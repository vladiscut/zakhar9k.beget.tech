import os

from django.db import models

class DocumentsFond(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    file = models.FileField(upload_to='documents/aboutfond/%Y/%m/%d/', verbose_name='Файл')
    is_fond = models.BooleanField(default=True, verbose_name='Документ о фонде')
    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Документ о фонде'
        verbose_name_plural = 'Документы о фонде'