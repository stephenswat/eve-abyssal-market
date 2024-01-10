from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("eve_auth.urls", namespace="eve_auth")),
    path("api/", include("abyssal_api.urls", namespace="abyssal_api")),
    path("faq/", TemplateView.as_view(template_name="help.html"), name="faq"),
    path("legal/", TemplateView.as_view(template_name="legal.html"), name="legal"),
    path(
        "support/", TemplateView.as_view(template_name="support.html"), name="support"
    ),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt")),
    path("", include("abyssal_modules.urls", namespace="abyssal_modules")),
    path("", include("django_prometheus.urls")),
]
