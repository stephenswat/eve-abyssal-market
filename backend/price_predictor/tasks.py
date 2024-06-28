import pickle
import logging
from django.utils import timezone
import datetime

from huey import crontab
from huey.contrib.djhuey import db_periodic_task, db_task

from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

from django.db.models import F

from abyssal_modules.models.modules import ModuleType, Module
from price_predictor.models import PricePredictor
from price_predictor.utils import predict_price


logger = logging.getLogger(__name__)


def create_model_for_type(t):
    mods = t.modules.annotate(
        contract_price=F("contracts__price"),
        contract_plex=F("contracts__plex"),
        contract_single=F("contracts__single_item"),
        contract_auction=F("contracts__auction"),
        contract_available=F("contracts__available"),
        contract_issued_at=F("contracts__issued_at"),
    ).filter(
        contract_single=True,
        contract_auction=False,
        contract_available=False,
        contract_contract_issued_at__gt=timezone.now() - datetime.timedelta(days=180),
    )

    logger.info(f"Creating price models for type {t.name}")

    if mods.count() < 50:
        logger.info(
            f"Abandoning model for {t.name} due to lack of modules ({mods.count()})"
        )
        return

    samples, features = [], []

    for x in mods:
        samples.append((x.contract_price + x.contract_plex * 5200000) / 1000000)
        features.append(x.attribute_vector())

    scaler = StandardScaler()
    scaler.fit(features)

    features = scaler.transform(features)

    reg = SVR(gamma=0.01, kernel="rbf", C=100000)
    scores = cross_val_score(reg, features, samples, cv=5)

    logger.info(
        "Created model for %s with accuracy %0.2f (+/- %0.2f, %d samples)"
        % (t.name, scores.mean(), scores.std() * 2, len(samples))
    )

    reg.fit(features, samples)

    PricePredictor(
        type=t,
        model=pickle.dumps(reg),
        scaler=pickle.dumps(scaler),
        quality=scores.mean(),
    ).save()


@db_periodic_task(crontab(minute="0", hour="0"))
def create_models():
    for t in ModuleType.objects.all():
        try:
            create_model_for_type(t)
        except Exception as e:
            logger.exception("Non-specified exception when creating module!")


@db_periodic_task(crontab(minute="0", hour="2"))
def clean_old_models():
    PricePredictor.objects.filter(
        date__lt=timezone.now() - datetime.timedelta(days=3)
    ).delete()


@db_task(retries=10, retry_delay=60)
def queue_price_prediction(module_id):
    module = Module.objects.filter(id=module_id).get()
    predict_price(module)
