# coding: utf-8

import uuid


class FYRequest:
    def __init__(self):
        self._cloudToken = None
        self._params = dict()
        self._body = dict()
        self._id = str(uuid.uuid4())
        self._version = '1.0'
        self._apiVer = '1.0.0'

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_version(self, version):
        self._version = version

    def get_version(self):
        return self._version

    def set_api_ver(self, api_ver):
        self._apiVer = api_ver

    def get_api_ver(self):
        return self._apiVer

    def set_cloud_token(self, cloud_token):
        self._cloudToken = cloud_token

    def get_cloud_token(self):
        return self._cloudToken

    def add_params(self, k, v):
        self._params[k] = v

    def get_params(self):
        return self._params

    def get_body(self):
        body = {
            "id": self.get_id(),
            "version": self.get_version(),
            "request": {
                "apiVer": self.get_api_ver(),
                "cloudToken": self.get_cloud_token()
            },
            "params": self.get_params()
        }
        return body
