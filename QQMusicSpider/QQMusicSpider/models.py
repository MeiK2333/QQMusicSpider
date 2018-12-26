import os

import pymongo


def MongoClientGenerator(host, port, username, password):
    client = pymongo.MongoClient(
        host=host, port=port, username=username, password=password)
    while True:
        yield client


mongo_client_dict = {}


def MongoClient(host=None, port=None, username=None, password=None):
    host = os.environ.get('MONGO_HOST', host)
    port = os.environ.get('MONGO_PORT', port)
    username = os.environ.get('MONGO_USERNAME', username)
    password = os.environ.get('MONGO_PASSWORD', password)

    client_str = f'{host}-{port}-{username}-{password}'

    if client_str not in mongo_client_dict.keys():
        mongo_client_dict[client_str] = MongoClientGenerator(
            host, port, username, password)

    return next(mongo_client_dict[client_str])
