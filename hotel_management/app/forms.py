from django import forms
from .models import register
class register_form(forms.ModelForm):
    class Meta:
        model=register
        fields='__all__'