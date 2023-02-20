from django.db import models

class Partners(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    photo = models.ImageField(upload_to='photos/partners/%Y/%m/%d/', blank=True, verbose_name='Изображение')
    url = models.URLField(blank=True, verbose_name='Ссылка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name= 'Дата редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Публиковать')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Партнеры'
        verbose_name_plural = 'Партнеры'