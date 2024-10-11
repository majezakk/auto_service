from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('dashboard:login')),  # Перенаправляем корневой путь на страницу авторизации
    path('', include('dashboard.urls')),  # Подключаем URL приложения dashboard
]
