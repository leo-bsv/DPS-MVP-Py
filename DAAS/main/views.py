from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CompanyForm
from .models import company

def home(request):
    return render(request, 'html/home.html')

def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            try:
                company.objects.create(
                    name=form.cleaned_data['name'],
                    inn=form.cleaned_data['inn'],
                )
                messages.success(request, 'Company Added Successfully')
                return redirect('profile')

            except IntegrityError:
                form.add_error('inn', 'ИНН уже занят')

        messages.error(request, 'Исправьте ошибки в форме.')

    else:
        form = CompanyForm()

    return render(request, 'html/company.html', {'form': form})
