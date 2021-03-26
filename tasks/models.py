from django.conf import settings
from django.db import models


class Task(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(verbose_name='Дедлайн', null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, 'task_owner')
    category = models.ForeignKey('categories.Category', models.CASCADE, 'category_task')

    def __str__(self):
        return self.title

