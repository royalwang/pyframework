# coding:utf-8


# 飞燕配置
FEIYAN = {
    'app_key': '',
    'app_secret': '',
    'host': 'https://api.link.aliyun.com',
    'grantType': 'project',     # 项目资源：授权类型
    'res': ''   # 项目资源：项目ID
}


# 阿里短信服务
SMS = {
    'default': {
        'access_key_id': '',
        'access_key_secret': '',
        'sign_name': '',
        'template_code': '',
        'template_param': {'code': None}
    }
}

# 阿里移动推送服务（不分端）
PUSH = {
    'default': {
        'access_key_id': 'xxx',
        'access_key_secret': 'xxx',
        'app_key': 'xxx'
    }
}
