from django import forms
from .models import FormData
from django.core.exceptions import ValidationError


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FormData
        exclude = []