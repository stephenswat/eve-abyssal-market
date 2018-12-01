from django.core.cache import cache
from django.http import JsonResponse, Http404
from django.views import View

from abyssal_modules.models import Module, ModuleType, StaticModule, EveCharacter


class AvailableTypedModuleListAPI(View):
    def get(self, request, type_id):
        try:
            module_type = ModuleType.objects.get(id=type_id)
        except ModuleType.DoesNotExist:
            raise Http404("Module type does not exist.")

        key = "AvailableTypedModuleListAPI_%d" % type_id

        res = cache.get(key)

        if res is None:
            res = [
                m.as_dict()
                for m in Module.available.filter(type=module_type)
            ]

            res += [
                m.as_dict()
                for m in StaticModule.objects.filter(type=module_type)
            ]

            cache.set(key, res, 60 * 15)

        return JsonResponse(res, safe=False)


class AvailableLatestModuleListAPI(View):
    def get(self, request):
        key = "AvailableLatestModuleListAPI"

        res = cache.get(key)

        if res is None:
            res = [
                m.as_dict()
                for m in Module.available.order_by('-first_seen')[:100]
            ]

            cache.set(key, res, 60 * 15)

        return JsonResponse(res, safe=False)


class CreatorModuleListAPI(View):
    def get(self, request, creator_id):
        try:
            creator = EveCharacter.objects.get(id=creator_id)
        except ModuleType.DoesNotExist:
            raise Http404("Creator does not exist.")

        return JsonResponse([
            m.as_dict()
            for m in creator.creations.all()
        ], safe=False)
