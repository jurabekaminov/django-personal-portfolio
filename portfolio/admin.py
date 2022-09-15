from django.contrib import admin
from .models import Project


admin.site.register(Project)  # Подключение модели Project к панели администратора
