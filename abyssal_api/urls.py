from django.urls import path

import abyssal_api.views as views


app_name = 'abyssal_api'


urlpatterns = [
    path('type/<int:type_id>/available/', views.AvailableTypedModuleListAPI.as_view(), name='module_list'),
    path('creator/<int:creator_id>/', views.CreatorModuleListAPI.as_view(), name='creator_list'),
    path('modules/latest/', views.AvailableLatestModuleListAPI.as_view(), name='lastest_modules'),
]
