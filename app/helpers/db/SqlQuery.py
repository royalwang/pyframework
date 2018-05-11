# coding:utf-8

from django.db import connection


def dict_fetchall(cursor):
    desc = cursor.description
    columns = [col[0] for col in desc]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def dict_fetchone(cursor):
    desc = cursor.description
    columns = [col[0] for col in desc]
    row = cursor.fetchone()
    return dict(zip(columns, row))


def fetchall(sql, params=()):
    cursor = connection.cursor()
    cursor.execute(sql, params)
    ret = dict_fetchall(cursor)
    cursor.close()
    return ret


def fetchone(sql, params=()):
    cursor = connection.cursor()
    cursor.execute(sql, params)
    ret = dict_fetchone(cursor)
    cursor.close()
    return ret


def execute(sql, params=()):
    cursor = connection.cursor()
    ret = cursor.execute(sql, params)
    cursor.close()
    return ret




