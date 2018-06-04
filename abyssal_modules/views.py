from django.shortcuts import render
from django.views import View

from abyssal_modules.models import Module

class ModuleList(View):
    def get(self, request):
        return render(
            request,
            'abyssal_modules/list.html',
            {
                'modules': Module.objects.all()[:50]
            }
        )
