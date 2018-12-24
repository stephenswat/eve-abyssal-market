import pickle

from huey import crontab
from huey.contrib.djhuey import db_periodic_task

from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

from django.db.models import F

from abyssal_modules.models.modules import ModuleType
from price_predictor.models import PricePredictor


def create_model_for_type(t):
    mods = t.modules.annotate(
        contract_price=F('contracts__price'),
        contract_plex=F('contracts__plex'),
        contract_single=F('contracts__single_item'),
        contract_auction=F('contracts__auction'),
        contract_available=F('contracts__available'),
        contract_sold=F('contracts__sold')
    ).filter(
        contract_single=True,
        contract_auction=False,
        contract_available=False,
        contract_sold=True
    )

    print("\n{:*^80}".format(t.name))

    if mods.count() < 50:
        print("Skipping due to lack of samples...")
        return

    samples, features = [], []

    for x in mods:
        samples.append((x.contract_price + x.contract_plex * 3300000) / 1000000)
        features.append(x.attribute_vector())

    scaler = StandardScaler()
    scaler.fit(features)

    features = scaler.transform(features)

    reg = SVR()

    param_grid = [
        {
            'C': [100, 1000, 10000, 100000, 1000000],
            'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
            'kernel': ['rbf']
        }
    ]

    clf = GridSearchCV(reg, param_grid, cv=3, iid=False)
    clf.fit(features, samples)
    print(clf.best_params_)

    reg = SVR(**clf.best_params_)
    scores = cross_val_score(reg, features, samples)
    print("Accuracy: %0.2f (+/- %0.2f, %d samples)" % (scores.mean(), scores.std() * 2, len(samples)))

    reg.fit(features, samples)

    PricePredictor(
        type=t,
        model=pickle.dumps(reg),
        scaler=pickle.dumps(scaler),
        quality=scores.mean()
    ).save()


@db_periodic_task(crontab(minute='0', hour='0'))
def create_models():
    for t in ModuleType.objects.all():
        try:
            create_model_for_type(t)
        except Exception:
            pass
