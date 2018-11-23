from django.contrib import admin

from contract_scanner.models import Contract, PlexPriceRecord


admin.site.register(Contract)
admin.site.register(PlexPriceRecord)
