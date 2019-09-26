from django import forms
from .models import sms,sms_login
class sms_form(forms.ModelForm):
    class Meta:
        model=sms
        fields='__all__'

class sms_login_form(forms.ModelForm):
    class Meta:
        model = sms_login
        fields = '__all__'
