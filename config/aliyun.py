# coding:utf-8


# 飞燕配置
FEIYAN = {
    'app_key': '24849450',
    'app_secret': '558cecf90c4bf99d16adbf02490a7e88',
    'host': 'https://api.link.aliyun.com',
    'grantType': 'project',     # 项目资源：授权类型
    'res': 'a1248ruzFF44pMTK'   # 项目资源：项目ID
}


# 阿里短信服务
SMS = {
    'default': {
        'access_key_id': 'LTAI7fpgbIgSBFI3',
        'access_key_secret': 'jIFUeOF2HatwFeG8xpOPLMHhFRtGK5',
        'sign_name': '镨安顿',
        'template_code': 'SMS_114595014',
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
