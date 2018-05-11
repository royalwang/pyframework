# coding:utf-8

from django.db import models


class AbstractModel(models.Model):
    appid = models.CharField(
        max_length=100,
        verbose_name='厂商标识',
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='更新时间'
    )

    class Meta:
        abstract = True
