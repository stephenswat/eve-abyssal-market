import threading
import logging

from django.conf import settings

from eve_esi.metrics import COUNTER_ESI_REQUESTS
from swagger_client.api_client import ApiClient
from eve_esi.exceptions import EsiException
from eve_auth.security import Security

logger = logging.getLogger(__name__)


class EsiManager:
    _ESI_APP = None
    _LOCK = threading.Lock()

    def _initialize_app(self):
        logger.debug("Initializing ESI app, attempting to acquire mutex lock...")
        self._LOCK.acquire()
        logger.debug("Mutex lock acquired!")

        if self._ESI_APP is None:
            logger.debug("Application still uninitialized. Initializing...")
            self._ESI_APP = ApiClient()
            logger.debug("Application initialized!")
        else:
            logger.debug("Another thread got here before us, nothing to be done!")

        self._LOCK.release()

    @property
    def app(self):
        if self._ESI_APP is None:
            self._initialize_app()
        return self._ESI_APP

    # def get_security(self):
    #     return esipy.EsiSecurity(
    #         # app=self.app,
    #         redirect_uri=settings.ESI_CALLBACK,
    #         client_id=settings.ESI_CLIENT_ID,
    #         secret_key=settings.ESI_SECRET_KEY,
    #         esi_datasource=getattr(settings, "ESI_DATASOURCE", "tranquility"),
    #         headers={"User-Agent": settings.ESI_USER_AGENT},
    #     )

    # def get_client(self, security=None):
    #     return esipy.EsiClient(
    #         security=security, headers={"User-Agent": settings.ESI_USER_AGENT}
    #     )

    # def __getitem__(self, key):
    #     return self.app.op[key]

    # def __request_helper(self, method, endpoint, client=None, **kwargs):
    #     if client is None:
    #         client = self.get_client()

    #     op = self[endpoint](**kwargs)

    #     if method == "head":
    #         res = client.head(op)
    #     elif method == "request":
    #         res = client.request(op)

    #     COUNTER_ESI_REQUESTS.labels(endpoint=endpoint, status=res.status).inc()

    #     if not 100 <= res.status <= 299:
    #         raise EsiException(endpoint, res.status, kwargs)

    #     return res

    # def head(self, endpoint, client=None, **kwargs):
    #     return self.__request_helper("head", endpoint, client, **kwargs)

    # def request(self, endpoint, client=None, multi_page=False, **kwargs):
    #     if not multi_page:
    #         return self.__request_helper("request", endpoint, client, **kwargs)

    #     res = []

    #     pages = self.head(endpoint, client, **kwargs).header["X-Pages"][0]

    #     for page in range(1, pages + 1):
    #         res += self.request(endpoint, client, page=page, **kwargs).data

    #     return res


ESI = EsiManager()
