from django.urls import path

import abyssal_api.views as views


app_name = 'abyssal_api'


urlpatterns = [
    path('type/<int:type_id>/available/', views.AvailableTypedModuleListAPI.as_view(), name='module_list'),
]
