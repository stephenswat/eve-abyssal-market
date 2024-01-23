from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.db.models import Count, F, Window
from django.db.models.functions import Trunc
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from abyssal_modules.models.modules import Module, ModuleType, StaticModule
from abyssal_modules.models.attributes import TypeAttribute
from abyssal_modules.models.characters import EveCharacter
from abyssal_modules.models.mutators import Mutator
from eve_esi import ESI
from eve_auth.models import EveUser
from price_predictor.models import PricePredictor
from abyssal_modules.forms import ModuleLinkForm
from abyssal_modules.tasks import create_module

class SimilarModuleRedirect(View):
    def get(self, request, module_id, type_id=None, referer=None):
        if referer == "assets":
            referer = "abyssal_modules:type_asset_module_list"
        elif referer == "contracts":
            referer = "abyssal_modules:type_module_list"
        else:
            # Default redirection.
            referer = "abyssal_modules:type_module_list"
        module = Module.objects.get(id=module_id)
        if type_id == None:
            type_id = module.type_id
        attributes = module.attribute_dict()
        parameters = ""
        data = request.GET
        for key in attributes.keys():
            if attributes[key]["display"]:
                if f"{key}_check" not in data.keys() or data[f"{key}_check"] == "true":
                    parameters += f"{key}={attributes[key]['real_value']}&"

        if "percent_range" in data.keys():
            parameters += f"percent_range={float(data['percent_range']) / 100}"
        else:
            parameters += f"percent_range=0.2"

        rev = reverse(referer, kwargs={"type_id": type_id})
        return HttpResponseRedirect(f"{rev}?{parameters}")


class ModuleList(View):
    def get(self, request):
        return render(
            request,
            "abyssal_modules/home.html",
        )


class TypedModuleList(View):
    def get(self, request, type_id):
        try:
            module_type = ModuleType.objects.get(id=type_id)
        except ModuleType.DoesNotExist:
            raise Http404("Module type does not exist.")

        attributes = module_type.attribute_list

        return render(
            request,
            "abyssal_modules/list.html",
            {"module_type": module_type, "attributes": attributes},
        )


class TypeAssetModuleList(LoginRequiredMixin, View):
    def get(self, request, type_id):
        try:
            module_type = ModuleType.objects.get(id=type_id)
        except ModuleType.DoesNotExist:
            raise Http404("Module type does not exist.")

        attributes = module_type.attribute_list

        return render(
            request,
            "abyssal_modules/asset_list.html",
            {"module_type": module_type, "attributes": attributes},
        )


class RollCalculatorView(View):
    def get(self, request, type_id):
        try:
            module_type = ModuleType.objects.get(id=type_id)
        except ModuleType.DoesNotExist:
            raise Http404("Module type does not exist.")

        mutators = Mutator.objects.filter(result=module_type).order_by(
            "item_type__name"
        )
        modules = StaticModule.objects.filter(type=module_type)
        attributes = TypeAttribute.objects.filter(
            mutatorattribute__mutator__result=module_type
        ).distinct("attribute")

        return render(
            request,
            "abyssal_modules/roll_calculator.html",
            {
                "module_type": module_type,
                "modules": modules,
                "mutators": mutators,
                "module_stats": {m.id: m.as_dict() for m in modules},
                "mutator_stats": {
                    m.item_type.id: {
                        x.attribute.attribute.id: (x.min_modifier, x.max_modifier)
                        for x in m.mutatorattribute_set.all()
                    }
                    for m in mutators
                },
                "attributes": attributes,
            },
        )


class ModuleView(DetailView):
    model = Module
    template_name = "abyssal_modules/module.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        static_modules = [m.as_dict() for m in StaticModule.objects.filter(type=self.object.type).all()]

        try:
            price_prediction = PricePredictor.predict_price(self.object)
        except Exception:
            price_prediction = None

        context["prediction"] = price_prediction
        context["contracts"] = self.object.contracts.all()

        module_attributes = self.object.as_dict()

        for v in static_modules:
            for k, vv in v["attributes"].items():
                if vv["display"]:
                    vv["delta"] = module_attributes["attributes"][k]["real_value"] - vv["real_value"]

        print(static_modules)

        context["static_modules"] = static_modules

        return context


class CreatorView(DetailView):
    model = EveCharacter
    template_name = "abyssal_modules/creator.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["modules"] = self.object.creations.all()
        return context


class AppraisalView(FormView):
    form_class = ModuleLinkForm
    template_name = "abyssal_modules/appraisal.html"

    def form_valid(self, form):
        type_id, item_id = form.cleaned_data["text"]

        module = create_module(type_id, item_id, priority=1000)(blocking=True)

        return HttpResponseRedirect(
            reverse("abyssal_modules:module_view", kwargs={"pk": module.id})
        )


class OpenContractView(LoginRequiredMixin, View):
    def post(self, request):
        try:
            character = request.user.characters.get(
                character_id=int(request.POST["character_id"])
            )
        except EveUser.DoesNotExist:
            return HttpResponse(status=403)

        ESI.request(
            "post_ui_openwindow_contract",
            client=character.get_client(),
            contract_id=int(request.POST["contract_id"]),
        )

        return HttpResponse(status=204)


class StatisticsList(View):
    def get(self, request):
        type_query = (
            Module.objects.values("type__name")
            .annotate(count=Count("id"))
            .order_by("-count")
        )

        type_breakdown = [(x["type__name"], x["count"]) for x in type_query[:20]]
        type_breakdown.append(("Other", sum(x["count"] for x in type_query[20:])))

        module_count_query = (
            Module.objects.annotate(hour=Trunc("first_seen", "day"))
            .annotate(cumsum=Window(expression=Count("id"), order_by=F("hour").asc()))
            .values("hour", "cumsum")
            .distinct("hour")
        )

        module_count_data = [
            (x["hour"].strftime(r"%Y%m%d"), x["cumsum"]) for x in module_count_query
        ]

        prolific_creators = EveCharacter.objects.annotate(
            creation_count=Count("creations")
        ).order_by("-creation_count")[:8]

        traded_modules = Module.objects.annotate(
            contract_count=Count("contracts")
        ).order_by("-contract_count")[:8]

        return render(
            request,
            "abyssal_modules/statistics.html",
            {
                "type_breakdown": type_breakdown,
                "module_count_data": module_count_data,
                "prolific_creators": prolific_creators,
                "traded_modules": traded_modules,
            },
        )
