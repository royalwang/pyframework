from config.rest_framework import REST_FRAMEWORK
import math
from app.helpers.db import SqlQuery

PAGE_SIZE = REST_FRAMEWORK['PAGE_SIZE']


def query(request, sql, values=()):
    page = 1
    if 'page' in request.GET and request.GET['page'].isdigit():
        page = int(request.GET['page'])
    data_all = SqlQuery.fetchall(sql, values)
    total = len(data_all)
    _data = data_all[(page - 1) * PAGE_SIZE:page * PAGE_SIZE]
    pages = int(math.ceil(float(total) / PAGE_SIZE))
    return {
        'total': total,
        'pages': pages,
        'current_page': page,
        'page_size': PAGE_SIZE,
        'data': _data
    }


def data(request, data_all):
    page = 1
    if 'page' in request.GET and request.GET['page'].isdigit():
        page = int(request.GET['page'])
    total = len(data_all)
    _data = data_all[(page - 1) * PAGE_SIZE:page * PAGE_SIZE]
    pages = int(math.ceil(float(total) / PAGE_SIZE))
    return {
        'total': total,
        'pages': pages,
        'current_page': page,
        'page_size': PAGE_SIZE,
        'data': _data
    }
