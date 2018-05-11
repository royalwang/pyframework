# coding:utf-8
import string

from django.contrib.auth.hashers import make_password, check_password
from django.db import models
from .AbstractModel import AbstractModel
import random


class User(AbstractModel):
    username = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='昵称'
    )
    phone = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name='手机'
    )
    email = models.EmailField(
        max_length=100,
        db_index=True,
        blank=True,
        verbose_name='邮箱'
    )
    password = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='密码'
    )
    openid = models.CharField(
        max_length=100,
        blank=True,
        unique=True,
        verbose_name='用户公开标识'
    )

    class Meta:
        db_table = 'z_user'
        unique_together = ('phone', 'appid')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.phone
        if not self.openid:
            self.openid = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(40))
        return super(User, self).save(*args, **kwargs)

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True
