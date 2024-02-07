from django.urls import path
from django.views.generic.base import RedirectView

import abyssal_modules.views


app_name = "abyssal_modules"

urlpatterns = [
    path(
        "type/<int:type_id>/<str:referer>/similar/<int:module_id>/",
        abyssal_modules.views.SimilarModuleRedirect.as_view(),
        name="similar_view",
    ),
    path(
        "module/<int:module_id>/similar/",
        abyssal_modules.views.SimilarModuleRedirect.as_view(),
        name="similar_view",
    ),
    path(
        "type/<int:type_id>/",
        RedirectView.as_view(
            pattern_name="abyssal_modules:type_module_list", permanent=True
        ),
    ),
    path(
        "type/<int:type_id>/contracts/",
        abyssal_modules.views.TypedModuleList.as_view(),
        name="type_module_list",
    ),
    path(
        "type/<int:type_id>/hof/",
        abyssal_modules.views.HallOfFameView.as_view(),
        name="type_hall_of_fame",
    ),
    path(
        "type/<int:type_id>/assets/",
        abyssal_modules.views.TypeAssetModuleList.as_view(),
        name="type_asset_module_list",
    ),
    path(
        "type/<int:type_id>/roll/",
        abyssal_modules.views.RollCalculatorView.as_view(),
        name="roll_calculator",
    ),
    path(
        "module/<int:pk>/",
        abyssal_modules.views.ModuleView.as_view(),
        name="module_view",
    ),
    path(
        "module/<int:pk>/image/",
        abyssal_modules.views.ModuleImageView.as_view(),
        name="module_image_view",
    ),
    path(
        "creator/<int:pk>/",
        abyssal_modules.views.CreatorView.as_view(),
        name="creator_view",
    ),
    path(
        "view_contract/",
        abyssal_modules.views.OpenContractView.as_view(),
        name="open_contract",
    ),
    path("appraisal/", abyssal_modules.views.AppraisalView.as_view(), name="appraisal"),
    path(
        "statistics/", abyssal_modules.views.StatisticsList.as_view(), name="statistics"
    ),
    path("", abyssal_modules.views.ModuleList.as_view()),
]
