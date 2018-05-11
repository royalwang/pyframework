# coding:utf-8

import binascii
import os
from django.db import models
from .AbstractModel import AbstractModel
from .User import User
from django.utils import timezone
import datetime
from config.token import Token as TokenSet
from app.helpers.api import ApiResponse
from rest_framework.exceptions import APIException


class Token(AbstractModel):
    access_token = models.CharField(
        max_length=255,
        verbose_name='Token令牌'
    )
    expires_in = models.IntegerField(
        verbose_name='有效期（秒）'
    )
    expires_at = models.DateTimeField(
        db_index=True,
        verbose_name='截至有效期'
    )
    refresh_token = models.CharField(
        max_length=255,
        verbose_name='刷新Token令牌'
    )
    invoked = models.BooleanField(
        default=False,
        verbose_name='是否销毁'
    )
    user = models.ForeignKey(
        User,
        db_index=True,
        on_delete=models.CASCADE,
        verbose_name='用户'
    )

    class Meta:
        db_table = 'z_token'

    def save(self, *args, **kwargs):
        if not self.access_token:
            self.access_token = binascii.hexlify(os.urandom(30)).decode()
        if not self.refresh_token:
            self.refresh_token = binascii.hexlify(os.urandom(30)).decode()
        if not self.expires_in:
            self.expires_in = TokenSet['expires_in']
        if not self.expires_at:
            self.expires_at = timezone.now() + datetime.timedelta(seconds=TokenSet['expires_in'])
        return super(Token, self).save(*args, **kwargs)

    @staticmethod
    def refresh(refresh_token):
        try:
            token = Token.objects.get(refresh_token=refresh_token)
            token.expires_at = timezone.now() + datetime.timedelta(seconds=TokenSet['expires_in'])
        except Token.DoesNotExist:
            raise APIException('The refresh_token is invalid')
        return token
