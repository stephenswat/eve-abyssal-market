import pickle

from django.db import models

from abyssal_modules.models.modules import ModuleType


class PricePredictor(models.Model):
    type = models.ForeignKey(ModuleType, models.CASCADE, db_index=True)
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    quality = models.FloatField()

    model = models.BinaryField()
    scaler = models.BinaryField()

    def unpickle(self):
        return pickle.loads(self.scaler), pickle.loads(self.model)

    @staticmethod
    def predict_price(module):
        model_row = PricePredictor.objects.filter(type=module.type).latest("date")

        scaler, model = model_row.unpickle()

        scaled_features = scaler.transform([module.attribute_vector()])

        return {
            "price": max(0, model.predict(scaled_features)[0] * 1000000),
            "confidence": model_row.quality,
        }
