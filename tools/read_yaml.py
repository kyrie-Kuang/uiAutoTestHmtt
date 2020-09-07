# -*- coding: utf-8 -*-
'''
相关功能：获取yaml数据
'''
import yaml
from config import BASE_PATH
import os


def read_yaml(filename):
    filepath = BASE_PATH + os.sep + "data" + os.sep + filename

    arr = []

    with open(filepath, "r", encoding="utf-8") as f:
        for data in yaml.safe_load(f).values():
            arr = tuple(data.values())
    return arr


if __name__ == '__main__':
    print(read_yaml("../data/tt_login.yaml"))
