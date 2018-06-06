from django.shortcuts import render
from django.views import View

from abyssal_modules.models import Module, ModuleType


class ModuleList(View):
    def get(self, request):
        return render(
            request,
            'abyssal_modules/list.html',
            {
                'modules': Module.objects.all()
            }
        )


class TypedModuleList(View):
    def get(self, request, type_id):
        module_type = ModuleType.objects.get(id=type_id)

        return render(
            request,
            'abyssal_modules/type_module_list.html',
            {
                'modules': module_type.modules.all(),
                'module_type': module_type,
                'attributes': module_type.attributes.filter(interesting=True).order_by('id').all()
            }
        )
