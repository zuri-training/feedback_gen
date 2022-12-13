from django import forms
from .models import FormData


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FormData
        exclude = []