from django.contrib import admin

from abyssal_modules.models import ModuleType, ModuleDogmaAttribute, Module


admin.site.register(ModuleType)
admin.site.register(ModuleDogmaAttribute)
admin.site.register(Module)
