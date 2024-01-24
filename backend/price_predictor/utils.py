import datetime

from price_predictor.models import PricePredictor, PricePredictionRecord

def predict_price(module):
    try:
        record = PricePredictionRecord.objects.filter(module=module).latest("date")

        age = datetime.datetime.now(datetime.timezone.utc) - record.date

        # Three days
        if age.total_seconds() >= 259200:
            record = None
    except PricePredictionRecord.DoesNotExist as e:
        record = None

    if record is None:
        try:
            model_row = PricePredictor.objects.filter(type=module.type).latest("date")

            scaler, model = model_row.unpickle()

            scaled_features = scaler.transform([module.attribute_vector()])

            price = max(0, model.predict(scaled_features)[0] * 1000000)

            record = PricePredictionRecord(
                module=module,
                model=model_row,
                price=price
            )

            record.save()
        except PricePredictor.DoesNotExist as e:
            pass

    if record is None:
        return None
    else:
        return record.price
