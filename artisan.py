#!/usr/bin/env python

import sys
import os

project_path = os.path.dirname(os.path.abspath(__file__))
controller_path = os.path.join(project_path, 'app/http/controllers')
model_path = os.path.join(project_path, 'databases/models')
serializer_path = os.path.join(project_path, 'app/http/serializers')
artisan_path = os.path.join(project_path, 'vendor/artisan')
console_choice = ('m', 'c', 'mc')

if len(sys.argv) < 3 or sys.argv[1][0:1] != '-' or sys.argv[1][1:] not in console_choice:
    print('console not found')
    exit()


def set_class_name(name, content):
    return content.replace('Example', name)


def get_name(base_dir, param):
    param_list = param.split('/')
    if len(param_list) > 1:
        path = os.path.join(base_dir, '/'.join(param_list[0: len(param_list) - 1]))
        if not os.path.exists(path):
            os.mkdir(path)
    return param_list[-1]


def make_controller(param, is_mc=False):
    name = get_name(controller_path, param)
    with open(os.path.join(controller_path, param + 'Controller.py'), 'w+') as f:
        with open(os.path.join(artisan_path, 'controller'), 'r') as r:
            lines = r.readlines()
            if not is_mc:
                lines[5] = ''
            f.write(set_class_name(name, ''.join(lines)).replace('serializers.', 'serializers.' + '.'.join(
                param.split('/')[0:len(param.split('/')) - 1]) + '.', 1))


def make_model(param, is_mc=False):
    name = get_name(model_path, param)
    if is_mc:
        param = name
    with open(os.path.join(model_path, param + '.py'), 'w+') as f:
        with open(os.path.join(artisan_path, 'model'), 'r') as r:
            f.write(set_class_name(name, r.read()))
        with open(os.path.join(model_path, '__init__.py'), 'a+') as a:
            content = 'from .%s import *' % '.'.join(param.split('/'))
            a.seek(0)
            if a.read().find(content) == -1:
                a.write('\n' + content)
    get_name(serializer_path, param)
    with open(os.path.join(serializer_path, param + 'Serializer.py'), 'w+') as f:
        with open(os.path.join(artisan_path, 'serializer'), 'r') as r:
            f.write(set_class_name(name, r.read()))


if sys.argv[1][1:] == 'c':
    make_controller(sys.argv[2])
elif sys.argv[1][1:] == 'm':
    make_model(sys.argv[2])
elif sys.argv[1][1:] == 'mc':
    make_model(sys.argv[2], True)
    make_controller(sys.argv[2], True)
