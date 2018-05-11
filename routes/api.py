# coding:utf-8

from django.urls import path
from app.http.controllers.api import AuthController, CodeController, UserInfoController, \
    FeiyanController

urlpatterns = [
    # 飞燕获取/刷新 access_token
    path('ali/get_access_token', FeiyanController.AliAccountToken.as_view()),
    # 飞燕获取用户信息
    path('ali/user_info', FeiyanController.AliAccountUserInfo.as_view()),
    # 飞燕获取设备数据
    path('ali/device_data', FeiyanController.AliDeviceData.as_view()),

    # 获取 Token
    path('access_token', AuthController.AccessToken.as_view()),
    # 刷新 Token
    path('refresh_token', AuthController.RefreshToken.as_view()),
    # 销毁 Token
    path('destroy_token', AuthController.DestroyToken.as_view()),
    # 获取验证码
    path('send_code', CodeController.SendCode.as_view()),
    # 设置密码
    path('reset_password', AuthController.ResetPassword.as_view()),
    # 用户信息
    path('user/info', UserInfoController.UserInfoDetail.as_view()),
]
