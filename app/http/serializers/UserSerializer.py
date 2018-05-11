# coding:utf-8


from rest_framework import serializers
from databases.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone', 'email')
