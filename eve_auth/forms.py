from django import forms
from django.core.exceptions import ValidationError


class LoginScopeForm(forms.Form):
    scope_open_contracts = forms.BooleanField(
        label="Open contracts in client",
        help_text="The app can open contracts (and other windows) in your EVE client.",
        required=False,
        initial=True
    )

    scope_read_contracts = forms.BooleanField(
        label="Read contracts",
        help_text="The app can read contracts that I have created and contracts which are available to me.",
        required=False,
        initial=True
    )

    scope_read_assets = forms.BooleanField(
        label="Read assets",
        help_text="The app can read my assets to find abyssal modules.",
        required=False,
        initial=False
    )

    def clean(self):
        cleaned_data = super().clean()

        scopes = []

        if cleaned_data['scope_open_contracts']:
            scopes.append('esi-ui.open_window.v1')

        if cleaned_data['scope_read_contracts']:
            scopes.append('esi-contracts.read_character_contracts.v1')

        if cleaned_data['scope_read_assets']:
            scopes.append('esi-assets.read_assets.v1')

        cleaned_data['scopes'] = scopes
        return cleaned_data
