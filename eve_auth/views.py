from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.shortcuts import redirect

from eve_esi import ESI


class LoginView(View):
    def get(self, request):
        return redirect(
            ESI.get_security().get_auth_uri(scopes=['esi-ui.open_window.v1'])
        )


class CallbackView(View):
    def get(self, request):
        security = ESI.get_security()

        tokens = security.auth(request.GET['code'])
        data = security.verify()

        login(request, authenticate(request, info=data, tokens=tokens))

        return redirect('/')
