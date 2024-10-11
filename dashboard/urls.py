from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('customers/', views.customer_list_view, name='customer_list'),
    path('customers/add/', views.add_customer_view, name='add_customer'),
    path('customers/edit/<int:customer_id>/', views.edit_customer_view, name='edit_customer'),
    path('customers/delete/<int:customer_id>/', views.delete_customer_view, name='delete_customer'),  # Удаление клиента
]
