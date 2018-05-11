# coding:utf-8

from rest_framework.views import APIView
from vendor.aliyun import sms
from databases.models import Code
import random
from app.helpers.api import ApiResponse
from config.aliyun import SMS
from databases.models import User

"""
发送验证码：
    请求参数：phone(手机), appid(厂商标识), flag(标签：短信类型; 1: 注册 2：修改密码)
    业务流程：
        1： 根据 phone, appid 查询用户信息
        2:  根据 flag 判断是否校验用户是否已注册
        3： 发送验证码
        4:  存储验证码
"""


class SendCode(APIView):
    authentication_classes = ()

    def post(self, request):
        if 'phone' not in request.data or 'appid' not in request.data:
            return ApiResponse.fail('The phone and appid param must be given', code=400)

        phone = request.data['phone']
        appid = request.data['appid']
        flag = request.data['flag'] if 'flag' in request.data else 0

        user = User.objects.filter(phone=phone, appid=appid)

        # 注册获取验证码,判断是否已注册
        if flag == 1 and user:
            return ApiResponse.fail('the phone is registered', code=10001)
        # 修改密码获取验证码,判断是否已注册
        elif flag == 2 and not user:
            return ApiResponse.fail('the phone is not registered', code=10002)

        number = random.randint(100000, 999999)

        # 获取短信服务信息
        params = SMS['default']
        params['template_param']['code'] = number

        # 发送短信
        res = sms.send(phone, **params)

        # 校验短信发成功结果, 成功则存储验证码
        if 'Code' in res and res['Code'] == 'OK':
            Code.objects.create(phone=phone, number=number)
            return ApiResponse.success()
        else:
            return ApiResponse.fail(res, code=10003)
