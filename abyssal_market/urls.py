from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('eve_auth.urls', namespace='eve_auth')),
    path('faq/', TemplateView.as_view(template_name="help.html"), name='faq'),
    path('legal/', TemplateView.as_view(template_name="legal.html"), name='legal'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt")),
    path('', include('abyssal_modules.urls', namespace='abyssal_modules'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
