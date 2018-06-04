from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.shortcuts import redirect

from eve_esi import ESI


class LoginView(View):
    def get(self, *args, **kwargs):
        return redirect(ESI.get_security().get_auth_uri(
            scopes=[
                'esi-contracts.read_character_contracts.v1',
                'esi-ui.open_window.v1'
            ]
        ))


class CallbackView(View):
    def get(self, request, *args, **kwargs):
        security = ESI.get_security()

        tokens = security.auth(request.GET['code'])
        data = security.verify()

        login(request, authenticate(request, info=data, tokens=tokens))

        return redirect('/')
