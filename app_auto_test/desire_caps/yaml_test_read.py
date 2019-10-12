#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_yaml_read.py
# @Author: LILIANG
# @Date  : 2019/9/16
# @Desc  :  test

import yaml

# fs=open("caps.yaml","r")
# datas=yaml.load(fs,yaml.FullLoader)
# print(datas)


fs=open("app_unnative_caps.yaml","r",encoding="utf-8")
datas=yaml.load(fs,yaml.FullLoader)
print(datas)

