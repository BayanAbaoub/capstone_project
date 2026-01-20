from .models import SubmitRequest
from django import forms


class SubmitForm(forms.ModelForm):
    class Meta:
        model = SubmitRequest
        fields = ('name', 'email', 'submission')