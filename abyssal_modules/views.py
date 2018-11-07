import datetime

from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.db.models import Min, Max, Count, F, Window
from django.db.models.functions import Trunc
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse

from abyssal_modules.models import (
    Module, ModuleType, ModuleAttribute, EveCharacter
)
from eve_esi import ESI
from price_predictor.models import PricePredictor
from abyssal_modules.forms import ModuleLinkForm
from abyssal_modules.tasks import create_module_helper


class ModuleList(View):
    def get(self, request):
        modules = Module.available.order_by('-first_seen')[:50]

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

        modules = Module.available.filter(type=module_type)
        attributes = module_type.attribute_list

        return render(
            request,
            'abyssal_modules/list.html',
            {
                'modules': modules,
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
        context['contracts'] = self.object.contracts.all()
        return context


class CreatorView(DetailView):
    model = EveCharacter
    template_name = 'abyssal_modules/creator.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modules'] = self.object.creations.all()
        return context


class AppraisalView(FormView):
    form_class = ModuleLinkForm
    template_name = 'abyssal_modules/appraisal.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        # return super().form_valid(form)

        type_id, item_id = form.cleaned_data['text']

        module = create_module_helper(type_id, item_id)

        return HttpResponseRedirect(
            reverse(
                'abyssal_modules:module_view',
                kwargs={'pk': module.id}
            )
        )



class OpenContractView(LoginRequiredMixin, View):
    def post(self, request):
        client = request.user.get_client().request(
            ESI['post_ui_openwindow_contract'](contract_id=int(request.POST['contract_id']))
        )

        return HttpResponse(status=204)


class StatisticsList(View):
    def get(self, request):
        type_query = Module.objects.values('type__name').annotate(count=Count('id')).order_by('-count')

        type_breakdown = [(x['type__name'], x['count']) for x in type_query[:20]]
        type_breakdown.append(('Other', sum(x['count'] for x in type_query[20:])))

        module_count_query = Module.objects.annotate(hour=Trunc('first_seen', 'day')).annotate(cumsum=Window(expression=Count('id'), order_by=F('hour').asc())).values('hour', 'cumsum').distinct('hour')
        module_count_data = [(x['hour'].strftime(r"%Y%m%d"), x['cumsum']) for x in module_count_query]

        prolific_creators = EveCharacter.objects.annotate(creation_count=Count('creations')).order_by('-creation_count')[:5]

        traded_modules = Module.objects.annotate(contract_count=Count('contracts')).order_by('-contract_count')[:5]

        return render(
            request,
            'abyssal_modules/statistics.html',
            {
                'type_breakdown': type_breakdown,
                'module_count_data': module_count_data,
                'prolific_creators': prolific_creators,
                'traded_modules': traded_modules,
            }
        )
