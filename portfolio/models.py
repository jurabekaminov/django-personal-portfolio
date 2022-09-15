from django.db import models


class Project(models.Model):
    # Класс, представляющий модель и обеспечивающий взаимодействие с БД в Django. Экземпляры класса будут в портфолио
    # Модель нужна для создания таблицы и добавления в нее данных

    # Атрибуты класса
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)  # параметр blank отвечает за открытие страницы в новой вкладке браузера

    def __str__(self):  # репрезентация проектов
        return self.title
