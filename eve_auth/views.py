from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.shortcuts import redirect

from eve_esi import get_esi_security


class LoginView(View):
    def get(self, *args, **kwargs):
        return redirect(get_esi_security().get_auth_uri(
            scopes=[
                'esi-contracts.read_character_contracts.v1',
                'esi-ui.open_window.v1'
            ]
        ))


class CallbackView(View):
    def get(self, request, *args, **kwargs):
        security = get_esi_security()

        tokens = security.auth(request.GET['code'])
        data = security.verify()

        login(request, authenticate(request, info=data, tokens=tokens))

        return redirect('/')
