from django.contrib.auth.models import AbstractUser
from django.db import models

from company.models import Company


class User(AbstractUser):
    """Модель пользователя"""
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                related_name='employees',
                                null=True,
                                blank=True
                                )
    REQUIRED_FIELDS = ('email', 'first_name', 'last_name', 'password',)

    def __str__(self):
        return self.username
