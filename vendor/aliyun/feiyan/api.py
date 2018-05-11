# coding: utf-8

from vendor.aliyun.feiyan import constant
from vendor.aliyun.feiyan import client
from vendor.aliyun.feiyan import request
import json
from vendor.aliyun.feiyan.FYRequest import FYRequest
from config.aliyun import FEIYAN


class Cloud:
    def __init__(self):
        self.host = FEIYAN['host']
        self.app_key = FEIYAN['app_key']
        self.app_secret = FEIYAN['app_secret']
        self.fy_request = FYRequest()

    # 实例化云端请求客户端对象
    def _client(self):
        return client.DefaultClient(app_key=self.app_key, app_secret=self.app_secret)

    # 实例化云端请求参数对象
    def _request(self, url):
        req_post = request.Request(host=self.host, protocol=constant.HTTP, url=url, method="POST")
        req_post.set_body(json.dumps(self.fy_request.get_body()))
        req_post.set_content_type(constant.CONTENT_TYPE_JSON)
        return req_post

    # 请求云端 API
    def _execute(self, url):
        return self._client().execute(self._request(url))

    # 获取云端资源Token
    def token(self):
        url = '/cloud/token'
        self.fy_request.add_params('grantType', FEIYAN['grantType'])
        self.fy_request.add_params('res', FEIYAN['res'])
        r = self._execute(url)
        print(r.json())

    # 刷新云端资源Token
    def refresh_token(self, token):
        url = '/cloud/token/refresh'
        self.fy_request.add_params('cloudToken', token)
        r = self._execute(url)
        print(r.json())

    # 查询物的产品列表
    def thing_product_list_get(self, page_size=15, page_no=1):
        url = '/cloud/thing/productList/get'
        self.fy_request.set_cloud_token(self.token())
        self.fy_request.add_params('pageSize', page_size)
        self.fy_request.add_params('pageNno', page_no)
        r = self._execute(url)
        print(r.json())

    # 查询物的产品
    def thing_product_get(self, product_key):
        url = '/cloud/thing/product/get'
        self.fy_request.set_cloud_token(self.token())
        self.fy_request.add_params('productKey', product_key)
        r = self._execute(url)
        print(r.json())

    # 获取物的属性
    def thing_properties_get(self, iot_id):
        url = '/cloud/thing/properties/get'
        self.fy_request.set_cloud_token(self.token())
        self.fy_request.add_params('iotId', iot_id)
        r = self._execute(url)
        print(r.json())

    # 获取物的模板
    def thing_tsl_get(self, iot_id):
        url = '/cloud/thing/tsl/get'
        self.fy_request.set_cloud_token(self.token())
        self.fy_request.add_params('iotId', iot_id)
        r = self._execute(url)
        print(r.json())

    # 触发物的服务
    def thing_service_invoke(self, iot_id, identifier, args):
        url = '/cloud/thing/service/invoke'
        self.fy_request.set_cloud_token(self.token())
        self.fy_request.add_params('iotId', iot_id)
        self.fy_request.add_params('identifier', identifier)
        self.fy_request.add_params('args', args)
        r = self._execute(url)
        print(r.json())

    # 设置物的属性
    def thing_properties_set(self, iot_id, items):
        url = '/cloud/thing/properties/set'
        self.fy_request.set_cloud_token(self.token())
        self.fy_request.add_params('iotId', iot_id)
        self.fy_request.add_params('items', items)
        r = self._execute(url)
        print(r.json())

    # 获取物的连接状态
    def thing_status_get(self, iot_id):
        url = '/cloud/thing/status/get'
        self.fy_request.set_cloud_token(self.token())
        self.fy_request.add_params('iotId', iot_id)
        r = self._execute(url)
        print(r.json())

    # 获取物
    def thing_info_get(self, iot_id):
        url = '/cloud/thing/info/get'
        self.fy_request.set_cloud_token(self.token())
        self.fy_request.add_params('iotId', iot_id)
        r = self._execute(url)
        print(r.json())

    # 批量获取物
    def things_info_get(self, product_key, status, current_page=1, page_size=15):
        url = '/cloud/things/info/get'
        self.fy_request.set_cloud_token(self.token())
        self.fy_request.add_params('productKey', product_key)
        self.fy_request.add_params('status', status)
        self.fy_request.add_params('currentPage', current_page)
        self.fy_request.add_params('pageSize', page_size)
        r = self._execute(url)
        print(r.json())

    # 分页查询用户列表
    def account_query_identity_by_page(self, offset=0, count=15):
        url = '/cloud/account/queryIdentityByPage'
        self.fy_request.set_cloud_token(self.token())
        self.fy_request.add_params('offset', offset)
        self.fy_request.add_params('count', count)
        r = self._execute(url)
        print(r.json())
