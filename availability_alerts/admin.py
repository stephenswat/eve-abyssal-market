from django.contrib import admin

from availability_alerts.models import AlertRequest, AlertRequestAttributes


admin.site.register(AlertRequest)
admin.site.register(AlertRequestAttributes)
