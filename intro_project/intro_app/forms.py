from typing import Any
from django import forms
from django.core import validators

class Webpage(forms.Form):
    topic = forms.CharField()
    name = forms.CharField(validators=[validators.MaxLengthValidator(50)])
    link = forms.URLField(assume_scheme="https")

    def clean(self) -> dict[str, Any]:
        webpage_form_data = super().clean()

        if webpage_form_data["topic"].startswith("A"):
            raise forms.ValidationError("Topic cannot start with A")