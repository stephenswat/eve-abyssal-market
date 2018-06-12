from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

import abyssal_modules.views


app_name = 'abyssal_modules'

urlpatterns = [
    path('type/<int:type_id>', abyssal_modules.views.TypedModuleList.as_view(), name='type_module_list'),
    path('module/<int:pk>', abyssal_modules.views.ModuleView.as_view(), name='module_view'),
    path('', abyssal_modules.views.ModuleList.as_view()),
]
