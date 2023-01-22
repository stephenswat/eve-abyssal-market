import re

from django import forms


class ModuleLinkForm(forms.Form):
    text = forms.CharField(label="Copied text", max_length=4000)

    def clean_text(self):
        match = re.search(r"<url=showinfo:(\d+)//(\d+)>", self.cleaned_data["text"])

        if match is None:
            raise forms.ValidationError("No module link found")

        return (int(match.group(1)), int(match.group(2)))
