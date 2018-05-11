# coding:utf-8

from django.utils import timezone
from rest_framework.views import APIView
from app.http.serializers.TokenSerializer import TokenSerializer
from app.helpers.api import ApiResponse
from databases.models import Token, User, Code
from rest_framework import permissions
from databases.models import UserInfo

"""
Token 生成，分为2中情况：
    1：请求参数 phone(手机), appid(厂商唯一标识), code(验证码)
       流程：通过 phone, code, appid, 以及当前时间校验数据库是否存在有效期内code,有则分配Token
    2: 请求参数 phone(手机), appid(厂商唯一标识), password(密码)
       流程：通过 phone, password, appid 校验账号,正确则分配Token
"""


class AccessToken(APIView):
    authentication_classes = ()
    serializer_class = TokenSerializer

    def post(self, request):
        if 'phone' not in request.data or 'appid' not in request.data:
            return ApiResponse.fail('The phone and appid param must be given', code=400)
        if 'code' not in request.data and 'password' not in request.data:
            return ApiResponse.fail('The password or code param must be given one', code=400)

        phone = request.data['phone']
        appid = request.data['appid']

        # 手机和密码校验身份
        if 'password' in request.data:
            password = request.data['password']
            try:
                user = User.objects.get(phone=phone, appid=appid)
            except User.DoesNotExist:
                return ApiResponse.fail('user does not found', code=404)
            if not user.check_password(password):
                return ApiResponse.fail('The password is invalid', code=400)

        # 手机和验证码校验身份
        else:
            code = request.data['code']
            try:
                Code.objects.get(phone=phone, number=code, invoked=False, expires_at__gt=timezone.now())
            except Code.DoesNotExist:
                return ApiResponse.fail('The code is invalid', code=400)

            # 创建用户时, 同时同步创建用户信息
            user, created = User.objects.get_or_create(phone=phone, appid=appid)
            if created:
                UserInfo.objects.create(user=user)

        # 创建 Token
        token = Token.objects.create(user=user)
        serializer = self.serializer_class(token)
        return ApiResponse.success(serializer.data)


"""
Token 刷新:
    请求参数 refresh_token
    根据 refresh_token 查询 Token 信息, 并更新 token 有效期
"""


class RefreshToken(APIView):
    authentication_classes = ()

    def post(self, request):
        if 'refresh_token' not in request.data:
            return ApiResponse.fail('The refresh_token param must be given', code=400)
        token = Token.refresh(request.data['refresh_token'])
        serializer = TokenSerializer(token)
        return ApiResponse.success(serializer.data)


"""
Token 销毁:
    直接将 token 表字段 invoked(是否销毁) 设置为 True
"""


class DestroyToken(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        token = request.auth
        token.invoked = True
        token.save()
        return ApiResponse.success()


"""
密码修改:
"""


class ResetPassword(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        if 'password' not in request.data:
            return ApiResponse.fail('The password param must be given', code=400)
        user = request.user
        user.set_password(request.data['password'])
        user.save()
        return ApiResponse.success()
