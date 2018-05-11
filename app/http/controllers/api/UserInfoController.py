# coding:utf-8

from rest_framework.views import APIView
from app.http.serializers.UserInfoSerializer import UserInfoSerializer, UserInfo
from app.helpers.api import ApiResponse
from rest_framework import permissions

"""
用户信息操作表:
    1: 用户信息包含2个表的数据，账号信息和用户其他个人信息
    2: 更新用户信息时，需要校验参数中是否存在账号信息相关数据:phone,email,username
       保证2个表的数据同步更新
"""


class UserInfoDetail(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserInfoSerializer

    def get(self, request):
        user_info = UserInfo.objects.get(user=request.user)
        data = self.serializer_class(user_info).data
        data['username'] = request.user.username
        data['phone'] = request.user.phone
        data['email'] = request.user.email
        return ApiResponse.success(data)

    def put(self, request):
        if 'phone' in request.data:
            request.user.phone = request.data['phone']
            request.data.pop('phone')
        if 'email' in request.data:
            request.user.email = request.data['email']
            request.data.pop('email')
        if 'username' in request.data:
            request.user.username = request.data['username']
            request.data.pop('username')
        request.user.save()

        obj = UserInfo.objects.get(user=request.user)
        request.data['user'] = request.user.id
        serializer = self.serializer_class(obj, request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            data['username'] = request.user.username
            data['phone'] = request.user.phone
            data['email'] = request.user.email
            return ApiResponse.success(data)
        else:
            return ApiResponse.fail(serializer.errors)
