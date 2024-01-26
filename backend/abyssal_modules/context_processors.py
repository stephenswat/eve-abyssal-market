from django.conf import settings


def google_analytics(request):
    return {"GA_TRACKING_ID": getattr(settings, "GA_TRACKING_ID", "")}


def google_adsense(request):
    return {
        "ADSENSE_PUBLISHER_ID": getattr(settings, "ADSENSE_PUBLISHER_ID", ""),
        "ADSENSE_SLOTS": getattr(settings, "ADSENSE_SLOTS", None),
    }
