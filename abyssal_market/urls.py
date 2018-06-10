from django.conf import settings

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('eve_auth.urls', namespace='eve_auth')),
    path('', include('abyssal_modules.urls', namespace='abyssal_modules'))
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns

print(__name__)
