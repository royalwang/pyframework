# coding:utf-8

from pymongo import MongoClient
from config.database import DATABASES

mongodb = DATABASES['mongodb']
HOST = mongodb['HOST']
PORT = mongodb['PORT']
NAME = mongodb['NAME']
USER = mongodb['USER']
PASSWORD = mongodb['PASSWORD']

connection = MongoClient(HOST, PORT)
mongo = connection[NAME]
mongo.authenticate(USER, PASSWORD)
