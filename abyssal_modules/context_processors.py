from django.conf import settings


def google_analytics(request):
    return {'GA_TRACKING_ID': getattr(settings, 'GA_TRACKING_ID', '')}
