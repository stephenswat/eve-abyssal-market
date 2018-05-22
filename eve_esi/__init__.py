import esipy

from django.conf import settings


ESI_APP = esipy.EsiApp(
    datasource=getattr(settings, 'ESI_DATASOURCE', 'tranquility')
)


ESI_SECURITY = esipy.EsiSecurity(
    app=ESI_APP.get_latest_swagger,
    redirect_uri=settings.ESI_CALLBACK,
    client_id=settings.ESI_CLIENT_ID,
    secret_key=settings.ESI_SECRET_KEY,
    esi_datasource=getattr(settings, 'ESI_DATASOURCE', 'tranquility'),
    headers={'User-Agent': settings.ESI_USER_AGENT}
)


ESI_CLIENT = esipy.EsiClient(
    security=ESI_SECURITY,
    headers={'User-Agent': settings.ESI_USER_AGENT}
)
