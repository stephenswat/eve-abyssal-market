from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.http import HttpResponse, FileResponse, Http404, HttpResponseRedirect
from django.db.models import Count, F, Window
from django.db.models.functions import Trunc
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.staticfiles import finders

from wand.color import Color
from wand.image import Image
from wand.drawing import Drawing
from wand.compat import nested

from abyssal_modules.models.modules import Module, ModuleType, StaticModule
from abyssal_modules.models.attributes import TypeAttribute
from abyssal_modules.models.characters import EveCharacter
from abyssal_modules.models.mutators import Mutator, MutatorAttribute
from eve_esi import ESI
from eve_auth.models import EveUser
from price_predictor.utils import predict_price
from abyssal_modules.forms import ModuleLinkForm
from abyssal_modules.tasks import create_module
from abyssal_modules.utils import (
    format_attribute_basic,
    render_attribute_value,
    correct_high_is_good,
)

import logging

logger = logging.getLogger(__name__)


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

        static_modules = [
            m.as_dict()
            for m in StaticModule.objects.filter(type=self.object.type).all()
        ]

        context["prediction"] = predict_price(self.object)
        context["contracts"] = self.object.contracts.all()
        context["image_url"] = self.request.build_absolute_uri(
            reverse("abyssal_modules:module_image_view", kwargs={"pk": self.object.id})
        )

        module_attributes = self.object.as_dict()

        for v in static_modules:
            for k, vv in v["attributes"].items():
                if vv["display"]:
                    vv["delta"] = (
                        module_attributes["attributes"][k]["real_value"]
                        - vv["real_value"]
                    )

        print(static_modules)

        context["static_modules"] = static_modules

        return context


class ModuleImageView(DetailView):
    model = Module
    response_class = FileResponse

    def render_to_response(self, context, **kwargs):
        BLOCK_DISTANCE = 4
        HEADER_HEIGHT = 96
        BLOCK_HEIGHT = 36
        STAT_BAR_HEIGHT = 4
        IMG_MARGINS = 4
        INNER_WIDTH = 352

        attr_dict = self.object.as_dict()

        base_module = StaticModule.objects.get(source_id=self.object.source_id)
        base_module_dict = base_module.as_dict()["attributes"]

        all_mutators = Mutator.objects.filter(result_id=self.object.type_id)

        mutator = Mutator.objects.get(item_type_id=self.object.mutator_id)

        mutator_dicts = {
            m.id: {
                v.attribute.attribute_id: (v.min_modifier, v.max_modifier)
                for v in MutatorAttribute.objects.filter(mutator_id=m.id)
            }
            for m in all_mutators
        }

        with Drawing() as draw:
            with Image(
                width=INNER_WIDTH + 2 * IMG_MARGINS,
                height=2 * IMG_MARGINS
                + len(mutator_dicts[mutator.id]) * (BLOCK_HEIGHT + BLOCK_DISTANCE)
                + HEADER_HEIGHT,
                format="png",
                background=Color("#020202"),
            ) as img:
                draw.font_family = "DejaVu Sans"
                draw.fill_color = Color("#ffffff")
                draw.text(10, 20, "Abyssal Ballistic Control System")
                draw.fill_color = Color("#28353b")
                draw.rectangle(
                    left=IMG_MARGINS,
                    top=IMG_MARGINS,
                    width=INNER_WIDTH - 1,
                    height=HEADER_HEIGHT - 1,
                )
                draw.font_size = 12
                draw.push()
                draw.fill_color = Color("#ffffff")
                draw.text(IMG_MARGINS + 32 + 2, 24, self.object.type.name)
                draw.text(IMG_MARGINS + 32 + 2, 24 + 32, self.object.source.name)
                draw.text(IMG_MARGINS + 32 + 2, 24 + 32 + 32, self.object.mutator.name)
                draw.pop()

                type_img_path = finders.find(
                    "img/types_32/%d.png" % self.object.type_id
                )
                if type_img_path is not None:
                    with Image(filename=type_img_path) as embed_img:
                        draw.composite(
                            operator="atop",
                            image=embed_img,
                            left=IMG_MARGINS,
                            top=IMG_MARGINS,
                            width=embed_img.width,
                            height=embed_img.height,
                        )

                source_img_path = finders.find(
                    "img/types_32/%d.png" % self.object.source_id
                )
                if source_img_path is not None:
                    with Image(filename=source_img_path) as embed_img:
                        draw.composite(
                            operator="atop",
                            image=embed_img,
                            left=IMG_MARGINS,
                            top=IMG_MARGINS + 32,
                            width=embed_img.width,
                            height=embed_img.height,
                        )

                mutator_img_path = finders.find(
                    "img/types_32/%d.png" % self.object.mutator_id
                )
                if mutator_img_path is not None:
                    with Image(filename=mutator_img_path) as embed_img:
                        draw.composite(
                            operator="atop",
                            image=embed_img,
                            left=IMG_MARGINS,
                            top=IMG_MARGINS + 64,
                            width=embed_img.width,
                            height=embed_img.height,
                        )

                i = 0

                for k in sorted(
                    mutator_dicts[mutator.id].keys(),
                    key=lambda x: attr_dict["attributes"][x]["name"].lower(),
                ):
                    v = attr_dict["attributes"][k]
                    if k in mutator_dicts[mutator.id]:
                        y = (
                            IMG_MARGINS
                            + HEADER_HEIGHT
                            + BLOCK_DISTANCE
                            + (BLOCK_HEIGHT + BLOCK_DISTANCE) * i
                        )

                        logger.info(k)

                        draw.rectangle(
                            left=IMG_MARGINS,
                            top=y,
                            width=INNER_WIDTH - 1,
                            height=BLOCK_HEIGHT - 1,
                        )
                        draw.push()
                        draw.fill_color = Color("#303030")
                        draw.rectangle(
                            left=IMG_MARGINS,
                            top=y + BLOCK_HEIGHT - STAT_BAR_HEIGHT,
                            width=INNER_WIDTH - 1,
                            height=STAT_BAR_HEIGHT - 1,
                        )
                        draw.pop()
                        draw.push()
                        delta = v["real_value"] - base_module_dict[k]["real_value"]
                        logger.info(delta)

                        v1 = (
                            float(mutator_dicts[mutator.id][k][0])
                            * base_module_dict[k]["real_value"]
                        )
                        v2 = (
                            float(mutator_dicts[mutator.id][k][1])
                            * base_module_dict[k]["real_value"]
                        )

                        mv1 = (
                            min(
                                float(mutator_dicts[x][k][0])
                                for x in mutator_dicts.keys()
                            )
                            * base_module_dict[k]["real_value"]
                        )
                        mv2 = (
                            max(
                                float(mutator_dicts[x][k][1])
                                for x in mutator_dicts.keys()
                            )
                            * base_module_dict[k]["real_value"]
                        )

                        if v["real_value"] >= 0:
                            min_mutated_value = v1
                            max_mutated_value = v2
                            min_bound_mutated_value = mv1
                            max_bound_mutated_value = mv2
                        else:
                            min_mutated_value = v2
                            max_mutated_value = v1
                            min_bound_mutated_value = mv2
                            max_bound_mutated_value = mv1

                        draw.push()
                        draw.fill_color = Color("#bf3438")
                        draw.pop()

                        if correct_high_is_good(v["high_is_good"], k):
                            max_left_delta = (
                                min_bound_mutated_value
                                - base_module_dict[k]["real_value"]
                            )
                            max_right_delta = (
                                max_bound_mutated_value
                                - base_module_dict[k]["real_value"]
                            )

                            if delta < 0:
                                max_delta = max_left_delta
                            else:
                                max_delta = max_right_delta

                            left_bound_delta = (
                                min_mutated_value - base_module_dict[k]["real_value"]
                            )
                            right_bound_delta = (
                                max_mutated_value - base_module_dict[k]["real_value"]
                            )
                            left_bound = (1 - (left_bound_delta / max_left_delta)) * (
                                INNER_WIDTH // 2
                            )
                            right_bound = (INNER_WIDTH // 2) + (
                                right_bound_delta / max_right_delta
                            ) * (INNER_WIDTH // 2)

                            if delta < 0:
                                draw.fill_color = Color("#bf3438")
                                left = (1 - (delta / max_delta)) * (INNER_WIDTH // 2)
                                right = INNER_WIDTH // 2
                            else:
                                draw.fill_color = Color("#69904f")
                                left = INNER_WIDTH // 2
                                right = (INNER_WIDTH // 2) + (delta / max_delta) * (
                                    INNER_WIDTH // 2
                                )
                        else:
                            max_right_delta = (
                                min_bound_mutated_value
                                - base_module_dict[k]["real_value"]
                            )
                            max_left_delta = (
                                max_bound_mutated_value
                                - base_module_dict[k]["real_value"]
                            )

                            if delta < 0:
                                max_delta = max_right_delta
                            else:
                                max_delta = max_left_delta

                            left_bound_delta = (
                                max_mutated_value - base_module_dict[k]["real_value"]
                            )
                            right_bound_delta = (
                                min_mutated_value - base_module_dict[k]["real_value"]
                            )
                            left_bound = (1 - (left_bound_delta / max_left_delta)) * (
                                INNER_WIDTH // 2
                            )
                            right_bound = (INNER_WIDTH // 2) + (
                                right_bound_delta / max_right_delta
                            ) * (INNER_WIDTH // 2)

                            if delta < 0:
                                draw.fill_color = Color("#69904f")
                                left = INNER_WIDTH // 2
                                right = (INNER_WIDTH // 2) + (delta / max_delta) * (
                                    INNER_WIDTH // 2
                                )
                            else:
                                draw.fill_color = Color("#bf3438")
                                left = (1 - (delta / max_delta)) * (INNER_WIDTH // 2)
                                right = INNER_WIDTH // 2
                        if right <= left:
                            right = left + 1
                            logger.error(
                                "Had to manually correct right-most edge of bar for attribute %d",
                                k,
                            )
                        draw.push()
                        draw.fill_color = Color("#445c66")
                        draw.rectangle(
                            left=IMG_MARGINS + left_bound,
                            right=IMG_MARGINS + right_bound - 1,
                            top=y + BLOCK_HEIGHT - STAT_BAR_HEIGHT,
                            height=STAT_BAR_HEIGHT - 1,
                        )
                        draw.pop()
                        draw.rectangle(
                            left=IMG_MARGINS + left,
                            right=right + IMG_MARGINS - 1,
                            top=y + BLOCK_HEIGHT - STAT_BAR_HEIGHT,
                            height=STAT_BAR_HEIGHT - 1,
                        )
                        draw.pop()
                        draw.push()
                        draw.fill_color = Color("#ffffff")
                        draw.text(IMG_MARGINS + 32 + 2, y + 13, v["name"])

                        value_str = "{val} {unit}".format(
                            val=format_attribute_basic(
                                render_attribute_value(v["real_value"], k), k
                            ),
                            unit=v["unit"],
                        )

                        metrics = draw.get_font_metrics(img, value_str)

                        draw.text(
                            IMG_MARGINS + 32 + 2,
                            y + 27,
                            value_str,
                        )
                        draw.pop()

                        draw.push()
                        draw.font_weight = 700
                        if correct_high_is_good(v["high_is_good"], k):
                            if delta < 0:
                                draw.fill_color = Color("#e63e43")
                            else:
                                draw.fill_color = Color("#72b348")
                        else:
                            if delta < 0:
                                draw.fill_color = Color("#72b348")
                            else:
                                draw.fill_color = Color("#e63e43")
                        rendered_delta = render_attribute_value(
                            v["real_value"], k
                        ) - render_attribute_value(base_module_dict[k]["real_value"], k)

                        if rendered_delta >= 0:
                            prefix = "+"
                        else:
                            prefix = ""

                        draw.text(
                            IMG_MARGINS + 32 + 2 + int(metrics.text_width) + 8,
                            y + 27,
                            "({prefix}{val} {unit})".format(
                                prefix=prefix,
                                val=format_attribute_basic(rendered_delta, k),
                                unit=v["unit"],
                            ),
                        )
                        draw.pop()

                        attr_img_path = finders.find("img/attributes_32/%d.png" % k)
                        if attr_img_path is not None:
                            with Image(filename=attr_img_path) as embed_img:
                                draw.composite(
                                    operator="atop",
                                    image=embed_img,
                                    left=IMG_MARGINS,
                                    top=y,
                                    width=embed_img.width,
                                    height=embed_img.height,
                                )
                        i += 1
                draw(img)

                return HttpResponse(
                    img.make_blob(format="png"), content_type="image/png"
                )


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
