#!/bin/bash

PROJECT_DIR=$(pwd)
ENV_DIR=$(dirname "$(dirname "$PROJECT_DIR")")

ps -ef | grep uwsgi | awk '{print $2}' | xargs kill -9

source $ENV_DIR/bin/activate

uwsgi --ini $PROJECT_DIR/uwsgi.ini

echo "===================== uwsgi 服务启动成功 ====================="

