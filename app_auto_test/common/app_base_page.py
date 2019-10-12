#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : app_base_page.py
# @Author: LILIANG
# @Date  : 2019/9/17
# @Desc  :  test

#app专属操作

from appium import webdriver
from common import useful_dir
from desire_caps import *
import yaml

from common import my_logger
logger=my_logger.my_logger(__file__)

class BasePageApp:

    def __init__(self):
        # self.driver=driver
        fs=open(useful_dir.caps_dir+'caps.yaml')
        caps=yaml.load(fs,Loader=yaml.FullLoader)
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
        self.driver.save_screenshot()



    #滑屏
    def swipe_screen(self):

        self.driver.swipe()

    #切换到webview
    def switch_to_contexts(self):
        self.driver
        pass

    #app处理toast
    def deal_toast(self):
        pass


    def touch_action(self):
        pass

    def get_app_element(self,loc,loc_msg=""):
        """
        :function:获取元素定位的对象
        :param loc: 元素定位表达式
        :param loc_msg: 功能页面page的描述
        :return: ele，返回一个定位到的元素对象
        """
        logger.info("获取 {} 的元素定位{}".format(loc_msg,loc))
        try:
            ele=self.driver.find_element(*loc)
            logger.info(" {} 元素定位成功".format(loc_msg))
            return ele
        except:
            logger.exception(" {} 元素定位失败".format(loc_msg))
            self.save_web_screenshot(loc_msg)
            raise



