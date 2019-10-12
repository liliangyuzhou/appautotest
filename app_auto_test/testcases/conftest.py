#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : conftest.py
# @Author: LILIANG
# @Date  : 2019/9/16
# @Desc  :  test

from appium import webdriver
from common import useful_dir
from desire_caps import *
import yaml
import pytest


#启动会话，每次不重置app
@pytest.fixture
def start_app():
    driver=base_driver()
    yield driver
    driver.close_app()


#启动会话，每次重置app
@pytest.fixture
def start_app_reset():
    driver=base_driver()
    yield driver
    driver.close_app()


@pytest.fixture
def login_app():
    # 启动会话
    driver=base_driver()
    yield driver


def base_driver(noReset=True,**kwargs):

    #从yaml文件中读取固定启动参数

    fs=open(useful_dir.caps_dir + '/caps.yaml')
    # fs=open('D:\\app_auto_test\\desire_caps\\caps.yaml')
    caps=yaml.load(fs,Loader=yaml.FullLoader)
    print(caps)

    #判断app是否重置，如果需要重置，修改字典中noReset的值
    if noReset is False:
        caps[noReset]=False
    #判断除了固定的启动参数之外，是否还会动态的传入关键字类的启动参数，如果有传入，动态全部写入请求参数caps的字典中
    #这里在测试app的webview页面可以用到
    if kwargs:
        for key,value in kwargs.items():
            caps[key]=value

    # 获取驱动driver
    driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
    return driver

if __name__=="__main__":
    # base_driver()
    start_app_reset()
