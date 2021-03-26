from django.conf import settings
from django.db import models


class Category(models.Model):
    title = models.CharField(verbose_name='Название категории', max_length=255)
    text = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, 'category_owner')

    def __str__(self):
        return self.title


