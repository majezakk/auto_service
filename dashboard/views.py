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

@login_required(login_url='dashboard:login')
@user_passes_test(is_admin, login_url='dashboard:login')
def vehicle_list_view(request):
    vehicles = Vehicle.objects.select_related('customer').all()
    return render(request, 'dashboard/vehicle_list.html', {'vehicles': vehicles})

@login_required(login_url='dashboard:login')
@user_passes_test(is_admin, login_url='dashboard:login')
def add_vehicle_view(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'dashboard/add_vehicle.html', {'form': form})

@login_required(login_url='dashboard:login')
@user_passes_test(is_admin, login_url='dashboard:login')
def edit_vehicle_view(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('dashboard:vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'dashboard/edit_vehicle.html', {'form': form, 'vehicle': vehicle})

@login_required(login_url='dashboard:login')
@user_passes_test(is_admin, login_url='dashboard:login')
def service_list_view(request):
    services = Service.objects.all()
    return render(request, 'dashboard/service_list.html', {'services': services})

@login_required(login_url='dashboard:login')
@user_passes_test(is_admin, login_url='dashboard:login')
def add_service_view(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:service_list')
    else:
        form = ServiceForm()
    return render(request, 'dashboard/add_service.html', {'form': form})

@login_required(login_url='dashboard:login')
@user_passes_test(is_admin, login_url='dashboard:login')
def edit_service_view(request, service_id):
    service = Service.objects.get(pk=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('dashboard:service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'dashboard/edit_service.html', {'form': form, 'service': service})

@login_required(login_url='dashboard:login')
@user_passes_test(is_admin, login_url='dashboard:login')
def employee_list_view(request):
    employees = Employee.objects.all()
    return render(request, 'dashboard/employee_list.html', {'employees': employees})

@login_required(login_url='dashboard:login')
@user_passes_test(is_admin, login_url='dashboard:login')
def add_employee_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'dashboard/add_employee.html', {'form': form})

@login_required(login_url='dashboard:login')
@user_passes_test(is_admin, login_url='dashboard:login')
def edit_employee_view(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('dashboard:employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'dashboard/edit_employee.html', {'form': form, 'employee': employee})

@login_required(login_url='dashboard:login')
@user_passes_test(is_admin, login_url='dashboard:login')
def delete_employee_view(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('dashboard:employee_list')
    return render(request, 'dashboard/delete_employee.html', {'employee': employee})

@login_required(login_url='dashboard:login')
@user_passes_test(is_admin, login_url='dashboard:login')
def delete_service_view(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        service.delete()
        return redirect('dashboard:service_list')
    return render(request, 'dashboard/delete_service.html', {'service': service})

@login_required(login_url='dashboard:login')
@user_passes_test(is_admin, login_url='dashboard:login')
def delete_vehicle_view(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('dashboard:vehicle_list')
    return render(request, 'dashboard/delete_vehicle.html', {'vehicle': vehicle})