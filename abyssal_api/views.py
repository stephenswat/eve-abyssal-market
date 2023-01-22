from django.core.cache import cache
from django.http import JsonResponse, Http404
from django.views import View

from rest_framework import serializers, generics, status, mixins
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from price_predictor.models import PricePredictor
from abyssal_modules.models.modules import Module, ModuleType, StaticModule
from abyssal_modules.models.attributes import ModuleAttributeView, ModuleDogmaAttribute
from abyssal_modules.models.characters import EveCharacter
from abyssal_modules.tasks import create_module
from eve_sde.models import InvType


"""
============================== OLD STYLE API ==================================
"""


class AvailableTypedModuleListAPI(View):
    def get(self, request, type_id):
        try:
            module_type = ModuleType.objects.get(id=type_id)
        except ModuleType.DoesNotExist:
            raise Http404("Module type does not exist.")

        key = "AvailableTypedModuleListAPI_%d" % type_id

        res = cache.get(key)

        if res is None:
            res = [m.as_dict() for m in Module.available.filter(type=module_type)]

            res += [m.as_dict() for m in StaticModule.objects.filter(type=module_type)]

            cache.set(key, res, 60 * 15)

        return JsonResponse(res, safe=False)


class AssetOwnedListAPI(View):
    def get(self, request, type_id):
        try:
            module_type = ModuleType.objects.get(id=type_id)
        except ModuleType.DoesNotExist:
            raise Http404("Module type does not exist.")

        if not request.user.is_authenticated:
            return JsonResponse([], safe=False)

        return JsonResponse(
            [
                m.as_dict()
                for m in Module.objects.filter(
                    type=module_type,
                    ownership_records__owner__character_id__in=request.user.eve.all_character_ids,
                )
            ],
            safe=False,
        )


class CreatorModuleListAPI(View):
    def get(self, request, creator_id):
        try:
            creator = EveCharacter.objects.get(id=creator_id)
        except ModuleType.DoesNotExist:
            raise Http404("Creator does not exist.")

        return JsonResponse([m.as_dict() for m in creator.creations.all()], safe=False)


"""
============================== NEW STYLE API ==================================
"""


class InvalidModuleCreationException(APIException):
    status_code = 400
    default_detail = "ESI claims such a module does not exist."
    default_code = "invalid_module"


class InvTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvType
        fields = ["id", "name"]
        read_only_fields = fields


class ModuleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleType
        fields = ["id", "name"]
        read_only_fields = fields


class EveCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EveCharacter
        fields = ["id", "name"]
        read_only_fields = fields


class DogmaAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleDogmaAttribute
        fields = ["id", "name"]
        read_only_fields = fields


class AttributeSerializer(serializers.ModelSerializer):
    dogma = DogmaAttributeSerializer(source="new_attribute.attribute")
    value = serializers.FloatField()
    rating = serializers.FloatField()

    class Meta:
        model = ModuleAttributeView
        fields = ["dogma", "value", "rating"]
        read_only_fields = fields


class ModuleSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="abyssal_api:module_detail")

    type = ModuleTypeSerializer(read_only=True)
    mutator = InvTypeSerializer(read_only=True)
    original = InvTypeSerializer(read_only=True, source="source")
    creator = EveCharacterSerializer(read_only=True)
    attributes = AttributeSerializer(
        many=True, read_only=True, source="attribute_values"
    )

    item_id = serializers.IntegerField(source="id", write_only=True)
    type_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Module
        fields = [
            "url",
            "id",
            "type",
            "mutator",
            "creator",
            "original",
            "attributes",
            "type_id",
            "item_id",
        ]
        extra_kwargs = {"id": {"read_only": True}}

    def create(self, validated_data):
        assert set(validated_data.keys()) == {"id", "type_id"}

        module = create_module(
            validated_data["type_id"],
            validated_data["id"],
            priority=1000,
        )(blocking=True)

        if module is None:
            raise InvalidModuleCreationException

        return module


class AppraisalSerializer(serializers.Serializer):
    price = serializers.FloatField()
    confidence = serializers.FloatField()


class ModuleDetailView(generics.RetrieveAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class CreatorDetailView(generics.RetrieveAPIView):
    queryset = EveCharacter.objects.all()
    serializer_class = EveCharacterSerializer


class CreatorCreationListView(generics.ListAPIView):
    serializer_class = ModuleSerializer

    def get_queryset(self):
        return Module.objects.filter(creator_id=self.kwargs["pk"])


class TypeListView(generics.ListAPIView):
    queryset = ModuleType.objects.all()
    serializer_class = ModuleTypeSerializer


class ModuleAppraisalView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = AppraisalSerializer

    def get(self, request, pk):
        try:
            module = Module.objects.get(pk=pk)
        except Module.DoesNotExist:
            return Response(
                {"error": "Module not found"}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            return Response(
                AppraisalSerializer(PricePredictor.predict_price(module)).data
            )
        except Exception:
            return Response({"error": "No prediction available"})


class ModuleView(generics.CreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
