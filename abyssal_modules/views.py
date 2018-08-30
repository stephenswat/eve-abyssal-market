import datetime

from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.http import HttpResponse, Http404
from django.db.models import Min, Max, Count, F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from abyssal_modules.models import (
    Module, ModuleType, ModuleAttribute, EveCharacter
)
from eve_esi import ESI

class ModuleList(View):
    def get(self, request):
        modules = (
            Module
            .objects
            .filter(
                contracts__available=True,
                contracts__expires_at__gte=timezone.now()
            )
            .annotate(
                contract_price=F('contracts__price'),
                contract_id=F('contracts__id'),
                contract_single=F('contracts__single_item'),
                contract_auction=F('contracts__auction')
            )
            .order_by('-first_seen')[:100]
        )

        return render(
            request,
            'abyssal_modules/list.html',
            {
                'modules': modules
            }
        )


class TypedModuleList(View):
    def get(self, request, type_id):
        try:
            module_type = ModuleType.objects.get(id=type_id)
        except ModuleType.DoesNotExist:
            raise Http404("Module type does not exist.")

        attributes = list(
            module_type.attributes
            .filter(interesting=True)
            .order_by('id')
            .all()
        )

        if (type_id == 47702):
            attributes.remove(module_type.attributes.get(id=2044))

        attribute_ranges = {
            x['attribute__id']: x
            for x in ModuleAttribute.objects
            .filter(
                module__type__id=type_id,
                attribute__in=attributes
            )
            .values('attribute__id')
            .annotate(min_val=Min('value'), max_val=Max('value'))
        }

        for a in attributes:
            mult = 0.001 if a.id == 73 else 1.0

            if a.id in attribute_ranges:
                offset = 0.02 * min(
                    abs(attribute_ranges[a.id]['max_val']), 
                    abs(attribute_ranges[a.id]['min_val'])
                )
                
                a.max_val = (attribute_ranges[a.id]['max_val'] + offset) * mult
                a.min_val = (attribute_ranges[a.id]['min_val'] - offset) * mult
            else:
                a.min_val = 0.0
                a.max_val = 100.0

        return render(
            request,
            'abyssal_modules/type_module_list.html',
            {
                'modules': module_type.modules.filter(
                    contracts__available=True,
                    contracts__expires_at__gte=timezone.now()
                ).annotate(
                    contract_price=F('contracts__price'),
                    contract_id=F('contracts__id'),
                    contract_single=F('contracts__single_item'),
                    contract_auction=F('contracts__auction')
                ),
                'module_type': module_type,
                'attributes': attributes
            }
        )


class ModuleView(DetailView):
    model = Module
    template_name = 'abyssal_modules/module.html'


class CreatorView(DetailView):
    model = EveCharacter
    template_name = 'abyssal_modules/creator.html'


class OpenContractView(LoginRequiredMixin, View):
    def post(self, request):
        client = request.user.get_client().request(
            ESI['post_ui_openwindow_contract'](contract_id=int(request.POST['contract_id']))
        )

        return HttpResponse(status=204)
