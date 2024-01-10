from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import abyssal_api.views as views


app_name = "abyssal_api"


schema_view = get_schema_view(
    openapi.Info(
        title="Abyssal API",
        default_version="v1",
        description="Test description",
        license=openapi.License(name="MIT License"),
    ),
    authentication_classes=[],
    public=True,
)

urlpatterns = [
    path(
        "old/type/<int:type_id>/available/",
        views.AvailableTypedModuleListAPI.as_view(),
        name="module_list",
    ),
    path(
        "old/type/<int:type_id>/assets/",
        views.AssetOwnedListAPI.as_view(),
        name="asset_list",
    ),
    path(
        "old/creator/<int:creator_id>/",
        views.CreatorModuleListAPI.as_view(),
        name="creator_list",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("modules/", views.ModuleView.as_view()),
    path("modules/<int:pk>/", views.ModuleDetailView.as_view(), name="module_detail"),
    path("modules/<int:pk>/appraisal/", views.ModuleAppraisalView.as_view()),
    path("types/", views.TypeListView.as_view()),
    path("creators/<int:pk>/", views.CreatorDetailView.as_view()),
    path("creators/<int:pk>/creations/", views.CreatorCreationListView.as_view()),
]
