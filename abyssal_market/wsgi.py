# flake8: noqa

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "abyssal_market.settings.local")

application = get_wsgi_application()
