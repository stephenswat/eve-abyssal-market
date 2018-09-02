import datetime

from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.http import HttpResponse, Http404
from django.db.models import Min, Max, Count, F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from abyssal_modules.models import (
    Module, ModuleType, ModuleAttribute, EveCharacter
)
from eve_esi import ESI
from price_predictor.models import PricePredictor


class ModuleList(View):
    def get(self, request):
        modules = Module.available.order_by('-first_seen')[:100]

        return render(
            request,
            'abyssal_modules/home.html',
            {'modules': modules}
        )


class TypedModuleList(View):
    def get(self, request, type_id):
        try:
            module_type = ModuleType.objects.get(id=type_id)
        except ModuleType.DoesNotExist:
            raise Http404("Module type does not exist.")

        attributes = list(
            module_type.attributes
            .filter(typeattribute__display=True)
            .annotate(high_is_good=F("typeattribute__high_is_good"))
            .order_by('id')
            .all()
        )

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
            if a.id == 73:
                mult = 0.001
            elif a.id == 1795:
                mult = 0.001
            elif a.id == 147:
                mult = 100
            else:
                mult = 1

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
            'abyssal_modules/list.html',
            {
                'modules': Module.available.filter(type=module_type),
                'module_type': module_type,
                'attributes': attributes
            }
        )


class ModuleView(DetailView):
    model = Module
    template_name = 'abyssal_modules/module.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            price_prediction = PricePredictor.predict_price(self.object)
        except Exception:
            price_prediction = None

        context['prediction'] = price_prediction
        return context


class CreatorView(DetailView):
    model = EveCharacter
    template_name = 'abyssal_modules/creator.html'


class OpenContractView(LoginRequiredMixin, View):
    def post(self, request):
        client = request.user.get_client().request(
            ESI['post_ui_openwindow_contract'](contract_id=int(request.POST['contract_id']))
        )

        return HttpResponse(status=204)


class HelpView(TemplateView):
    template_name = 'abyssal_modules/help.html'
