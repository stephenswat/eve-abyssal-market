from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('eve_auth.urls', namespace='eve_auth')),
    path('', include('abyssal_modules.urls', namespace='abyssal_modules'))
]
