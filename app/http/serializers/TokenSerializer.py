# coding:utf-8

from rest_framework import serializers
from databases.models import Token


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('access_token', 'expires_in', 'expires_at', 'refresh_token')
