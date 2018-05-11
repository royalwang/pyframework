# 基于 django 2.0 的自制框架


### 介绍
* 将 django 框架目录结构做了调整
* 配置文件拆分
* 路由分类
* 异常信息回调重构
* model 抛离应用，重定义 model 开发层级
* api 回调格式统一
* 自定义 auth 认证相关表
* uwsgi 服务重启脚本
* vendor 第三方类库
* 原生 SQL，MongoDB 函数简单封装
* 自定义分页类
* 通用账号体系


###  建议
* 建议使用 virtualenv 虚拟环境;
* 项目根目录 run.sh 作为 uwsgi 服务重启文件
* 项目部署后, 给予 run.sh 可执行权限 chmod +x run.sh

### 安装

```
apt install python3.5
apt install python3.5-dev

apt install python3-pip
pip install --upgrade pip

apt install libmysqlclient-dev

pip install -r package.txt
```


