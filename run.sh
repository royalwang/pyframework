#!/bin/bash

ps -ef | grep uwsgi | awk '{print $2}' | xargs kill -9

source /opt/env3/bin/activate

uwsgi --ini /opt/env3/projects/pyframework/uwsgi.ini

echo "===================== uwsgi 服务启动成功 ====================="

