import os
from uuid import uuid1

from django.db import models
from django.urls import reverse



class Projects(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='images/projects/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    content = models.TextField(verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name= 'Дата редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Публиковать на главную')
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'

    def get_absolute_url(self):
        return reverse('project', kwargs = {'proj_slug': self.slug})

class News(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name='Проект')
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='images/projects/news/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    content = models.TextField(verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Публиковать')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'



class Documents(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name='Проект')
    title = models.CharField(max_length=255, verbose_name='Название')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    file = models.FileField(upload_to='documents/projects/%Y/%m/%d/', verbose_name='Файл')
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'