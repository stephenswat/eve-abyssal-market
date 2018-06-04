from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.shortcuts import redirect, render

from eve_esi import ESI
from eve_auth.forms import LoginScopeForm


class LoginView(View):
    def get(self, request):
        return render(
            request,
            'eve_auth/login.html',
            {'form': LoginScopeForm()}
        )

    def post(self, request):
        form = LoginScopeForm(request.POST)

        if not form.is_valid():
            return redirect('/')

        return redirect(
            ESI.get_security().get_auth_uri(scopes=form.cleaned_data['scopes'])
        )


class CallbackView(View):
    def get(self, request):
        security = ESI.get_security()

        tokens = security.auth(request.GET['code'])
        data = security.verify()

        login(request, authenticate(request, info=data, tokens=tokens))

        return redirect('/')
