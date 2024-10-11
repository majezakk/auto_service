from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('customers/', views.customer_list_view, name='customer_list'),
    path('customers/add/', views.add_customer_view, name='add_customer'),
    path('customers/edit/<int:customer_id>/', views.edit_customer_view, name='edit_customer'),
    path('customers/delete/<int:customer_id>/', views.delete_customer_view, name='delete_customer'),
    path('vehicles/', views.vehicle_list_view, name='vehicle_list'),
    path('vehicles/add/', views.add_vehicle_view, name='add_vehicle'),
    path('vehicles/edit/<int:vehicle_id>/', views.edit_vehicle_view, name='edit_vehicle'),
    path('vehicles/delete/<int:vehicle_id>/', views.delete_vehicle_view, name='delete_vehicle'),
    path('services/', views.service_list_view, name='service_list'),
    path('services/add/', views.add_service_view, name='add_service'),
    path('services/edit/<int:service_id>/', views.edit_service_view, name='edit_service'),
    path('services/delete/<int:service_id>/', views.delete_service_view, name='delete_service'),
    path('employees/', views.employee_list_view, name='employee_list'),
    path('employees/add/', views.add_employee_view, name='add_employee'),
    path('employees/edit/<int:employee_id>/', views.edit_employee_view, name='edit_employee'),
    path('employees/delete/<int:employee_id>/', views.delete_employee_view, name='delete_employee'),
]

