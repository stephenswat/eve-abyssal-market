from django import template


register = template.Library()


@register.filter()
def prediction_confidence(conf):
    if conf > 0.98:
        return "Extremely high"
    elif conf > 0.95:
        return "Very high"
    elif conf > 0.90:
        return "High"
    elif conf > 0.80:
        return "Moderate"
    elif conf > 0.70:
        return "Low"
    elif conf > 0.50:
        return "Very low"
    elif conf > 0.25:
        return "Extremely low"
    else:
        return "Completely garbage"
