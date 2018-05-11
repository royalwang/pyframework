# coding: utf-8

"""
此文件函数，用于回调格式统一；
成功回调 success: code码默认为 0；
失败回调 fail: code码默认为 10000，建议调用该函数时，自定义错误码，并更新文档上错误码信息
"""

from rest_framework.response import Response


def success(message='', status='success', code=0):
    return Response({
        'code': code,
        'status': status,
        'message': message
    })


def fail(message='', code=10000, status='fail'):
    return Response({
        'code': code,
        'status': status,
        'message': message
    })
