import esipy

from django.conf import settings


ESI_APP = esipy.EsiApp(
    datasource=getattr(settings, 'ESI_DATASOURCE', 'tranquility')
)


def get_esi_security():
    return esipy.EsiSecurity(
        app=ESI_APP.get_latest_swagger,
        redirect_uri=settings.ESI_CALLBACK,
        client_id=settings.ESI_CLIENT_ID,
        secret_key=settings.ESI_SECRET_KEY,
        esi_datasource=getattr(settings, 'ESI_DATASOURCE', 'tranquility'),
        headers={'User-Agent': settings.ESI_USER_AGENT}
    )


def get_esi_client(security=None):
    return esipy.EsiClient(
        security=security,
        headers={'User-Agent': settings.ESI_USER_AGENT}
    )
