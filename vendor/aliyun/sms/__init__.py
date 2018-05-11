# coding:utf-8

from vendor.aliyun.utils import rpc_signature
import time
import urllib.request
import json


def send(phone_numbers, **kwargs):
    access_key_id = kwargs['access_key_id']
    access_key_secret = kwargs['access_key_secret']
    sign_name = kwargs['sign_name']
    template_code = kwargs['template_code']
    template_param = kwargs['template_param']
    url = 'http://dysmsapi.aliyuncs.com'
    params = {
        'Action': 'SendSms',
        'Version': '2017-05-25',
        'RegionId': 'cn-hangzhou',
        'PhoneNumbers': phone_numbers,
        'SignName': sign_name,
        'TemplateCode': template_code,
        'TemplateParam': template_param,
        'OutId': int(time.time() * pow(10, 3))
    }
    request_url = rpc_signature.get_signed_url(url, access_key_id, access_key_secret, params)
    req = urllib.request.Request(request_url)
    res = urllib.request.urlopen(req).read().decode('utf-8')
    return json.loads(res)
