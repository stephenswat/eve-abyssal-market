from django.urls import path

import abyssal_modules.views


app_name = 'abyssal_modules'

urlpatterns = [
    path(
        'type/<int:type_id>',
        abyssal_modules.views.TypedModuleList.as_view(),
        name='type_module_list'
    ),
    path(
        'module/<int:pk>',
        abyssal_modules.views.ModuleView.as_view(),
        name='module_view'
    ),
    path(
        'creator/<int:pk>',
        abyssal_modules.views.CreatorView.as_view(),
        name='creator_view'
    ),
    path(
        'view_contract',
        abyssal_modules.views.OpenContractView.as_view(),
        name='open_contract'
    ),
    path(
        '',
        abyssal_modules.views.ModuleList.as_view()
    ),
]
