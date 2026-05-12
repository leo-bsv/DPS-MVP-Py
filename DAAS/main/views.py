from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import AddUserByEmailForm
from django.db import IntegrityError
from django.contrib import messages
from .forms import CompanyForm
from .models import company

def home(request):
    return render(request, 'html/home.html')

def comp_list(request):
    return render(request, 'html/company_list.html')

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


def add_user_to_project(request, project_id):
    project = get_object_or_404(company, id=project_id)
    form = AddUserByEmailForm(request.POST or None)

    # 3. Логика обработки
    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data['email']
        user_to_add = User.objects.filter(email=email).first()

        if not user_to_add:
            messages.error(request, "Пользователь с таким email не найден.")
        elif project.users.filter(id=user_to_add.id).exists():
            messages.warning(request, f"Пользователь уже добавлен в {project.name}.")
        else:
            project.users.add(user_to_add)
            messages.success(request, f"Готово! {user_to_add.username} теперь в команде.")
            return redirect('company_list', project_id=project.id)

    # 4. Рендеринг (и для GET, и для невалидного POST)
    return render(request, 'company_list.html', {
        'form': form,
        'project': project
    })

def models_s(request):
    return render(request, 'html/models.html')

def orders_view(request):
    return render(request, 'html/orders.html')