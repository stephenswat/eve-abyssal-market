from django.http import JsonResponse, Http404
from django.views import View
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from abyssal_modules.models import Module, ModuleType


@method_decorator(cache_page(60 * 10), name='dispatch')
class AvailableTypedModuleListAPI(View):
    def get(self, request, type_id):
        try:
            module_type = ModuleType.objects.get(id=type_id)
        except ModuleType.DoesNotExist:
            raise Http404("Module type does not exist.")

        return JsonResponse([
            {
                'id': m.id,
                'attributes': m.attribute_dict_with_derived(),
                'contract': {
                    'id': m.contract_id,
                    'price': {
                        'isk': m.contract_price,
                        'plex': m.contract_plex,
                        'total': m.contract_price_inc_plex
                    },
                    'auction': m.contract_auction,
                    'multi_item': not m.contract_single
                },
                'pyfa': m.get_pyfa_string()
            }
            for m in Module.available.filter(type=module_type)
        ], safe=False)
