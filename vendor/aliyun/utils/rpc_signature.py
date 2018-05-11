# coding=utf-8

import base64
import hashlib
import hmac
import time
import uuid
from urllib import parse, request


def get_uuid():
    return str(uuid.uuid4())


def get_iso_8061_date():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def get_signer_name():
    return "HMAC-SHA1"


def get_singer_version():
    return "1.0"


def get_sign_string(source, secret):
    h = hmac.new(bytes(secret, encoding='utf-8'), bytes(source, encoding='utf-8'), hashlib.sha1)
    signature = base64.b64encode(h.digest())
    return signature


# 添加基础参数
def __refresh_sign_parameters(access_key_id):
    parameters = dict()
    parameters["Timestamp"] = get_iso_8061_date()
    parameters["SignatureMethod"] = get_signer_name()
    parameters["SignatureVersion"] = get_singer_version()
    parameters["SignatureNonce"] = get_uuid()
    parameters["AccessKeyId"] = access_key_id
    parameters["Format"] = 'JSON'
    return parameters


# Url 编码整合
def __pop_standard_urlencode(query):
    ret = parse.urlencode(query)
    ret = ret.replace('+', '%20')
    ret = ret.replace('*', '%2A')
    ret = ret.replace('%7E', '~')
    return ret


# 获取签名所需拼接字符串
def __compose_string_to_sign(method, queries):
    sorted_parameters = sorted(queries.items(), key=lambda e: e[0])
    string_to_sign = method + "&%2F&" + request.pathname2url(__pop_standard_urlencode(sorted_parameters))
    return string_to_sign


# 生成签名
def __get_signature(string_to_sign, secret):
    return get_sign_string(string_to_sign, secret + '&')


# 返回接口域名后所需参数
def get_signed_url(url, access_key_id, access_key_secret, params, method='GET'):
    url_params = __refresh_sign_parameters(access_key_id)
    sign_params = dict(url_params)
    sign_params.update(params)
    string_to_sign = __compose_string_to_sign(method, sign_params)
    signature = __get_signature(string_to_sign, access_key_secret)
    sign_params['Signature'] = signature
    request_url = url + '/?' + __pop_standard_urlencode(sign_params)
    return request_url
