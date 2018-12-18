from django.contrib import admin

from abyssal_modules.models.modules import ModuleType, Module
from abyssal_modules.models.attributes import ModuleDogmaAttribute, TypeAttribute
from abyssal_modules.models.characters import EveCharacter


admin.site.register(ModuleType)
admin.site.register(ModuleDogmaAttribute)
admin.site.register(Module)
admin.site.register(EveCharacter)
admin.site.register(TypeAttribute)
