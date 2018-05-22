import os
from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dev'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ESI_SWAGGER_JSON = "https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility"
ESI_CALLBACK = ""
ESI_CLIENT_ID = ""
ESI_SECRET_KEY = ""
ESI_USER_AGENT = ""
