# coding:utf-8

from django.db import models
from .User import User
from .AbstractModel import AbstractModel


class UserInfo(AbstractModel):
    SEX_CHOICES = (
        (0, '女'),
        (1, '男'),
        (2, '保密')
    )

    avatar = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='头像'
    )
    birthday = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='生日'
    )
    sex = models.CharField(
        max_length=3,
        default=2,
        choices=SEX_CHOICES,
        verbose_name='性别'
    )
    city = models.CharField(
        max_length=10,
        blank=True,
        verbose_name='城市'
    )
    address = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='住址'
    )
    company = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='公司'
    )
    job = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='职位'
    )
    name = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='姓名'
    )
    age = models.IntegerField(
        default=0,
        verbose_name='年龄'
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='用户'
    )

    class Meta:
        db_table = 'z_user_info'
