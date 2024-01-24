import pickle

from django.db import models

from abyssal_modules.models.modules import ModuleType, Module


class PricePredictor(models.Model):
    type = models.ForeignKey(ModuleType, models.CASCADE, db_index=True)
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    quality = models.FloatField()

    model = models.BinaryField()
    scaler = models.BinaryField()

    def unpickle(self):
        return pickle.loads(self.scaler), pickle.loads(self.model)


class PricePredictionRecord(models.Model):
    module = models.ForeignKey(Module, models.CASCADE, db_index=True)
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    model = models.ForeignKey(PricePredictor, models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=32, decimal_places=2, db_index=True)
