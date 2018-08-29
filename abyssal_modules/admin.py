from django.contrib import admin

from abyssal_modules.models import ModuleType, ModuleDogmaAttribute, Module, EveCharacter


admin.site.register(ModuleType)
admin.site.register(ModuleDogmaAttribute)
admin.site.register(Module)
admin.site.register(EveCharacter)
