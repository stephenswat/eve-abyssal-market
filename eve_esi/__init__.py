import esipy

from django.conf import settings


ESI_APP = esipy.App.create(settings.ESI_SWAGGER_JSON)


ESI_SECURITY = esipy.EsiSecurity(
    app=ESI_APP,
    redirect_uri=settings.ESI_CALLBACK,
    client_id=settings.ESI_CLIENT_ID,
    secret_key=settings.ESI_SECRET_KEY,
)


ESI_CLIENT = esipy.EsiClient(
    security=ESI_SECURITY,
    headers={'User-Agent': settings.ESI_USER_AGENT}
)
