from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.shortcuts import redirect

from eve_esi import ESI_SECURITY


class LoginView(View):
    def get(self, *args, **kwargs):
        return redirect(ESI_SECURITY.get_auth_uri())


class CallbackView(View):
    def get(self, request, *args, **kwargs):
        ESI_SECURITY.auth(request.GET['code'])
        data = ESI_SECURITY.verify()

        user = authenticate(
            request,
            character_id=data['CharacterID'],
            name=data['CharacterName']
        )

        login(request, user)

        return redirect('/')
