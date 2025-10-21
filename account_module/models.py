from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    avatar = models.CharField(max_length=20, verbose_name='تصویر آواتار', blank=True, null=True)
    email_active_code1 = models.TextField(max_length=70, verbose_name='کد فعالسازی ایمیل')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()
