from django import forms


class ScopeForm(forms.Form):
    scope_open_window = forms.BooleanField(
        label='Open windows',
        help_text='Allow the site to open contract windows.',
        required=False,
        initial=True,
        disabled=True,
    )
    scope_read_assets = forms.BooleanField(
        label='Read assets',
        help_text='Allow the site to read my assets.',
        required=False,
        initial=True,
    )
