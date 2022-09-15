from django.contrib import admin
from .models import Blog


admin.site.register(Blog)  # Подключение модели Blog к панели администратора
