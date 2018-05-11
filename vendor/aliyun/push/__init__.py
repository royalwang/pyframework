# coding:utf-8

from vendor.aliyun.utils import rpc_signature
import urllib.request
import json


def send(target_value, title, body, push_type='NOTICE', target='DEVICE', **kwargs):
    access_key_id = kwargs['access_key_id']
    access_key_secret = kwargs['access_key_secret']
    app_key = kwargs['app_key']
    url = 'http://cloudpush.aliyuncs.com'
    params = {
        'Action': 'Push',
        'Version': '2016-08-01',
        'RegionId': 'cn-hangzhou',
        'AppKey': app_key,  # 推送不分端 AppKey
        'DeviceType': 'ALL',  # 不分端
        'PushType': push_type,  # MESSAGE：表示消息, NOTICE：表示通知
        'Target': target,  # DEVICE:根据设备推送, ACCOUNT:根据账号推送, ALIAS:根据别名推送, TAG:根据标签推送, ALL:推送给全部设备
        'TargetValue': target_value,  # 根据Target来设定，多个值使用逗号分隔，超过限制需要分多次推送
        'Title': title,  # 标题
        'Body': body  # 内容

    }
    request_url = rpc_signature.get_signed_url(url, access_key_id, access_key_secret, params)
    req = urllib.request.Request(request_url)
    res = urllib.request.urlopen(req).read().decode('utf-8')
    return json.loads(res)
