# coding:utf-8

import datetime
from django.db import models
from django.utils import timezone
from .AbstractModel import AbstractModel


class Code(AbstractModel):
    number = models.CharField(
        max_length=6,
        verbose_name='验证码'
    )
    phone = models.CharField(
        max_length=11,
        verbose_name='手机号'
    )
    expires_at = models.DateTimeField(
        verbose_name='截至有效期'
    )
    invoked = models.IntegerField(
        default=0,
        verbose_name='是否销毁'
    )

    class Meta:
        db_table = 'z_code'

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + datetime.timedelta(seconds=15 * 60)
        return super(Code, self).save(*args, **kwargs)
