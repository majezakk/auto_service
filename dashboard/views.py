from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:  # Проверяем, что пользователь является администратором
                login(request, user)
                return redirect('dashboard:home')  # перенаправление после успешного входа
            else:
                error_message = "У вас нет прав доступа. Вход только для администраторов."
                return render(request, 'dashboard/login.html', {'error': error_message})
        else:
            error_message = "Неверное имя пользователя или пароль"
            return render(request, 'dashboard/login.html', {'error': error_message})

    return render(request, 'dashboard/login.html')


# Функция проверки, является ли пользователь администратором
def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required(login_url='dashboard:login')  # Требуется вход в систему
@user_passes_test(is_admin, login_url='dashboard:login')  # Требуется статус администратора
def home_view(request):
    # Здесь будет логика домашней страницы, CRUD функциональность и т.д.
    return render(request, 'dashboard/home.html')


@login_required(login_url='dashboard:login')  # Требуется вход в систему
@user_passes_test(is_admin, login_url='dashboard:login')  # Требуется статус администратора
def customer_list_view(request):
    customers = Customer.objects.all()  # Получаем всех клиентов
    return render(request, 'dashboard/customer_list.html', {'customers': customers})


@login_required(login_url='dashboard:login')  # Требуется вход в систему
@user_passes_test(is_admin, login_url='dashboard:login')  # Требуется статус администратора
def add_customer_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:customer_list')
    else:
        form = CustomerForm()
    return render(request, 'dashboard/add_customer.html', {'form': form})

@login_required(login_url='dashboard:login')  # Требуется вход в систему
@user_passes_test(is_admin, login_url='dashboard:login')  # Требуется статус администратора
def edit_customer_view(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('dashboard:customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'dashboard/edit_customer.html', {'form': form, 'customer': customer})

@login_required(login_url='dashboard:login')  # Требуется вход в систему
@user_passes_test(is_admin, login_url='dashboard:login')  # Требуется статус администратора
def delete_customer_view(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('dashboard:customer_list')
    return render(request, 'dashboard/delete_customer.html', {'customer': customer})