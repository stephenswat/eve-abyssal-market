# flake8: noqa

import os
import logging
import yaml

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "eve_auth",
    "eve_esi",
    "eve_sde",
    "eve_mail_queue",
    "abyssal_api",
    "abyssal_modules",
    "asset_scanner",
    "contract_scanner",
    "price_predictor",
    "huey.contrib.djhuey",
    "django_bootstrap5",
    "rest_framework",
    "drf_yasg",
    "django_prometheus",
    "django_redis",
    "django.contrib.humanize",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
]

ROOT_URLCONF = "abyssal_market.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "abyssal_modules.context_processors.google_analytics",
                "eve_auth.context_processors.user_eve_characters",
            ],
        },
    },
]

# Default settings
BOOTSTRAP5 = {
    "theme_url": "/static/css/theme.css",
}

WSGI_APPLICATION = "abyssal_market.wsgi.application"

AUTHENTICATION_BACKENDS = [
    "eve_auth.backend.EveAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
]

AUTH_USER_MODEL = "auth.User"

LOGIN_URL = "/auth/login"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

TIME_ZONE = "UTC"

USE_I18N = False

USE_TZ = True

DATETIME_FORMAT = "F j, Y, H:i"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
}

with open("/run/secrets/postgres_password", "r") as f:
    _POSTGRES_PW = f.read().strip()

with open("/run/secrets/configuration", "r") as f:
    _CONFIG = yaml.safe_load(f)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = _CONFIG["DEBUG"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = _CONFIG["SECRET_KEY"]

ALLOWED_HOSTS = ([_CONFIG["HOSTNAME"]] if "HOSTNAME" in _CONFIG else []) + [
    "127.0.0.1",
    "localhost",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "mutaplasmid",
        "USER": "postgres",
        "PASSWORD": _POSTGRES_PW,
        "HOST": "postgres",
        "PORT": "",
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

LOGGING = {
    "version": 1,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.StreamHandler",
        },
        "file_django": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "/logs/django.log",
            "maxBytes": 10**8,
            "backupCount": 5,
        },
        "file_huey": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "/logs/huey.log",
            "maxBytes": 10**8,
            "backupCount": 5,
        },
        "file_other": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "/logs/other.log",
            "maxBytes": 10**8,
            "backupCount": 5,
        },
        "file_market": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "/logs/market.log",
            "maxBytes": 10**8,
            "backupCount": 5,
        },
        "file_esi": {
            "level": "DEBUG",
            "formatter": "standard",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "/logs/esi.log",
            "maxBytes": 10**8,
            "backupCount": 5,
        },
    },
    "loggers": {
        "": {"level": "INFO", "handlers": ["console", "file_other"]},
        "abyssal_api": {
            "level": "INFO",
            "handlers": ["console", "file_market"],
            "propagate": False,
        },
        "abyssal_market": {
            "level": "INFO",
            "handlers": ["console", "file_market"],
            "propagate": False,
        },
        "abyssal_modules": {
            "level": "INFO",
            "handlers": ["console", "file_market"],
            "propagate": False,
        },
        "asset_scanner": {
            "level": "INFO",
            "handlers": ["console", "file_market"],
            "propagate": False,
        },
        "contract_scanner": {
            "level": "INFO",
            "handlers": ["console", "file_market"],
            "propagate": False,
        },
        "eve_auth": {
            "level": "INFO",
            "handlers": ["console", "file_market"],
            "propagate": False,
        },
        "eve_esi": {
            "level": "INFO",
            "handlers": ["console", "file_market"],
            "propagate": False,
        },
        "eve_mail_queue": {
            "level": "INFO",
            "handlers": ["console", "file_market"],
            "propagate": False,
        },
        "eve_sde": {
            "level": "INFO",
            "handlers": ["console", "file_market"],
            "propagate": False,
        },
        "price_predictor": {
            "level": "INFO",
            "handlers": ["console", "file_market"],
            "propagate": False,
        },
        "huey": {
            "level": "INFO",
            "handlers": ["console", "file_huey"],
            "propagate": False,
        },
        "huey.consumer": {
            "level": "INFO",
            "handlers": ["console", "file_huey"],
            "propagate": False,
        },
        "django": {
            "level": "INFO",
            "handlers": ["console", "file_django"],
            "propagate": False,
        },
        "pyswagger": {
            "level": "INFO",
            "handlers": ["console", "file_esi"],
            "propagate": False,
        },
    },
}

if "SENTRY_DSN" in _CONFIG:
    import sentry_sdk

    from sentry_sdk.integrations.logging import LoggingIntegration
    from sentry_sdk.integrations.redis import RedisIntegration
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=_CONFIG["SENTRY_DSN"],
        integrations=[
            LoggingIntegration(level=logging.INFO, event_level=logging.WARNING),
            RedisIntegration(),
            DjangoIntegration(),
        ],
        environment=_CONFIG.get("ENVIRONMENT_NAME", "unknown"),
        traces_sample_rate=0.2,
    )

    LOGGING["handlers"]["sentry"] = {
        "level": "WARNING",
        "class": "sentry_sdk.integrations.logging.SentryHandler",
    }

    for l in LOGGING["loggers"]:
        LOGGING["loggers"][l]["handlers"].append("sentry")

GA_TRACKING_ID = _CONFIG.get("GA_TRACKING_ID", None)

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/4",
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        "KEY_PREFIX": "mutaplasmid.cache",
    }
}

HUEY = {
    "consumer": {"workers": 8, "worker_type": "thread"},
    "huey_class": "huey.PriorityRedisHuey",
    "connection": {"host": "redis"},
    "immediate": False,
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

STATIC_ROOT = "/static"

ESI_SWAGGER_JSON = "https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility"
ESI_CALLBACK = _CONFIG["ESI_CALLBACK_ROOT"] + "auth/callback/"

ESI_CLIENT_ID = _CONFIG["ESI_CLIENT_ID"]
ESI_SECRET_KEY = _CONFIG["ESI_SECRET_KEY"]

ESI_USER_AGENT = _CONFIG["ESI_USER_AGENT"]
