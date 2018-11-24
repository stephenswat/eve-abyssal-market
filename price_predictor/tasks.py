import pickle

from huey import crontab
from huey.contrib.djhuey import db_periodic_task

from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

from django.db.models import F

from abyssal_modules.models import ModuleType
from price_predictor.models import PricePredictor


@db_periodic_task(crontab(minute='0', hour='0'))
def create_models():
    for t in ModuleType.objects.all():
        mods = t.modules.annotate(
            contract_price=F('contracts__price'),
            contract_single=F('contracts__single_item'),
            contract_auction=F('contracts__auction')
        ).filter(contract_single=True, contract_auction=False)

        if mods.count() < 50:
            continue

        samples, features = [], []

        for x in mods:
            samples.append(x.contract_price / 1000000)
            features.append([y.value for y in x.attribute_list])

        scaler = StandardScaler()
        scaler.fit(features)

        features = scaler.transform(features)

        print("\n{:*^80}".format(t.name))

        reg = SVR()

        param_grid = [
            {
                'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000],
                'gamma': [1000, 100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 1e-7, 1e-8, 1e-9, 1e-10],
                'kernel': ['rbf']},
        ]

        clf = GridSearchCV(reg, param_grid)
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
