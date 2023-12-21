from django.conf import settings


def google_analytics(request):
    return {"GA_TRACKING_ID": getattr(settings, "GA_TRACKING_ID", "")}

def google_adsense(request):
    return {"ADSENSE_OWNER_TAG": getattr(settings, "ADSENSE_OWNER_TAG", "")}
