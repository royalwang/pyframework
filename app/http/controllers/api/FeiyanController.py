# coding: utf-8

from rest_framework.views import APIView
from config.aliyun import FEIYAN
from app.helpers.api import ApiResponse
from app.http.serializers.TokenSerializer import Token
from rest_framework.response import Response
from django.utils import timezone
from databases.models import UserInfo


# 飞燕自建账号 get_access_token
class AliAccountToken(APIView):
    permission_classes = ()

    def post(self, request):
        grant_type = request.GET['grant_type']
        client_id = request.GET['client_id']
        client_secret = request.GET['client_secret']
        code = request.GET['code']
        if client_id != FEIYAN['app_key'] or client_secret != FEIYAN['app_secret']:
            return ApiResponse.fail()
        token = None
        if grant_type == 'authorization_code':
            token = Token.objects.get(access_token=code)
        elif grant_type == 'refresh_token':
            refresh_token = request.GET['refresh_token ']
            token = Token.refresh(refresh_token)
        return Response({
            'result_code': '0',
            'access_token': token.access_token,
            'expires_in': str(token.expires_in),
            'refresh_token': token.refresh_token,
            'openid': token.user.openid
        })


# 飞燕自建账号 user_info
class AliAccountUserInfo(APIView):
    def post(self, request):
        access_token = request.GET['access_token']
        openid = request.GET['openid']
        try:
            Token.objects.select_related('user').get(
                access_token=access_token,
                expires_at__gt=timezone.now(),
                invoked=False
            )
            user_info = UserInfo.objects.get(user__openid=openid)
            return Response({
                "result_code": "0",
                "message": "成功",
                "openid": user_info.user.openid,
                "nick_name": user_info.user.username,
                "gender": str(user_info.sex)
            })
        except Token.DoesNotExist:
            return ApiResponse.fail()


# 飞燕接收数据
class AliDeviceData(APIView):
    def post(self, request):
        print(request.data)
        return Response({
            "code": 200,
            "message": "success",
            "data": "OK"
        })
