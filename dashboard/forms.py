from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'phone', 'email', 'address']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone': 'Телефон',
            'email': 'Электронная почта',
            'address': 'Адрес',
        }
        help_texts = {
            'phone': 'Пожалуйста, укажите контактный номер телефона.',
            'email': 'Укажите действующий адрес электронной почты.',
        }

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['customer', 'make', 'model', 'year', 'license_plate']
        labels = {
            'customer': 'Владелец',
            'make': 'Марка',
            'model': 'Модель',
            'year': 'Год выпуска',
            'license_plate': 'Номерной знак',
        }
        help_texts = {
            'year': 'Укажите год выпуска транспортного средства.',
            'license_plate': 'Укажите регистрационный номер транспортного средства.',
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_name', 'description', 'price_per_hour']
        labels = {
            'service_name': 'Название услуги',
            'description': 'Описание',
            'price_per_hour': 'Цена за час',
        }
        help_texts = {
            'price_per_hour': 'Укажите стоимость выполнения услуги за один час.',
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'position', 'salary']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'position': 'Должность',
            'salary': 'Зарплата',
        }
        help_texts = {
            'position': 'Укажите занимаемую должность сотрудника.',
            'salary': 'Укажите зарплату в рублях.',
        }
