from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.shortcuts import redirect, render

from eve_esi import ESI
from eve_auth.forms import ScopeForm


class LoginView(View):
    def get(self, request):
        return render(
            request,
            'eve_auth/scope_selection.html',
            {'form': ScopeForm()}
        )

    def post(self, request):
        form = ScopeForm(request.POST)

        if not form.is_valid():
            return redirect('/')

        print(form.cleaned_data)

        scopes = []

        if form.cleaned_data['scope_open_window']:
            scopes.append('esi-ui.open_window.v1')

        if form.cleaned_data['scope_read_assets']:
            scopes.append('esi-assets.read_assets.v1')

        return redirect(
            ESI.get_security().get_auth_uri(scopes=scopes)
        )


class CallbackView(View):
    def get(self, request):
        security = ESI.get_security()

        tokens = security.auth(request.GET['code'])
        data = security.verify()

        login(request, authenticate(request, info=data, tokens=tokens))

        return redirect('/')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(
            request,
            'eve_auth/profile.html',
            {
                'user': request.user,
                'characters': request.user.characters
            }
        )
