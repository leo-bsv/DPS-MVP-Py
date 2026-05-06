from django.contrib import admin
from .models import company
from django import forms

class CompanyForm(forms.ModelForm):
    class Meta:
        model = company
        fields = '__all__'
        widgets = {
            'inn': forms.NumberInput(attrs={'style': 'width: 50ch;'})}

@admin.register(company)
class CompanyAdmin(admin.ModelAdmin):
    form = CompanyForm
    list_display = ('name', 'inn', 'in_created')
    list_filter = ('in_created',)
    search_fields = ('name',)
