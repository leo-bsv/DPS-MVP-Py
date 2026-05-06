from django import forms
from django.core.validators import RegexValidator

class CompanyForm(forms.Form):
    name = forms.CharField(max_length=100)
    inn = forms.CharField(max_length=12, validators=[RegexValidator('[0-9]+')],)