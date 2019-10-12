#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_login.py
# @Author: LILIANG
# @Date  : 2019/9/20
# @Desc  :  test
from common import basepage
import pytest
from page_objects.login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_locators import login_locators as lc

from testdatas.login_data import *



@pytest.mark.usefixtures("start_app")
class TestLogin:

    #
    # @pytest.mark.smoke
    # def test_add(self):
    #     print(1+1)

    # @pytest.mark.smoke("未注册的手机号")
    # def test_login_error_uesr(self, start_app):
    #     # WebDriverWait(start_app,30).until(EC.visibility_of_element_located(lc.my_image_locator))
    #     LoginPage(start_app).login_before()
    #     LoginPage(start_app).login('13736815921', '8159231')
    #     res = LoginPage(start_app).get_toast_text(lc.toast_loc)
    #     print(res)
    #     assert res == "错误的账号信息"
    #
    # @pytest.mark.smoke
    # def test_login_error_passwd(self, start_app):
    #     # WebDriverWait(start_app,30).until(EC.visibility_of_element_located(lc.my_image_locator))
    #     LoginPage(start_app).login_before()
    #     LoginPage(start_app).login('13736815923', '8159231')
    #     res = LoginPage(start_app).get_toast_text(lc.toast_loc)
    #     print(res)
    #     assert res == "错误的账号信息"
    #
    #
    #
    # @pytest.mark.smoke
    # def test_login_success(self,start_app):
    #     # WebDriverWait(start_app,30).until(EC.visibility_of_element_located(lc.my_image_locator))
    #     LoginPage(start_app).login_before()
    #     LoginPage(start_app).login('13736815923','815923')
    #     res=LoginPage(start_app).get_element_text(lc.login_success_my_schedue)
    #     print(res)
    #     assert res=='本周课表'


    @pytest.mark.smoke
    @pytest.mark.parametrize("data",login_data_fail)
    def test_login_failed(self,data,start_app):
        # WebDriverWait(start_app,30).until(EC.visibility_of_element_located(lc.my_image_locator))
        LoginPage(start_app).login_before()
        LoginPage(start_app).login(data['user'],data['password'])
        res=LoginPage(start_app).get_toast_text(lc.toast_loc)
        print(res)
        assert res==data["check"]

    @pytest.mark.smoke

    def test_login_success(self,start_app):
        # WebDriverWait(start_app,30).until(EC.visibility_of_element_located(lc.my_image_locator))
        LoginPage(start_app).login_before()
        LoginPage(start_app).login(login_data_success['user'], login_data_success['password'])
        res = LoginPage(start_app).get_element_text(lc.login_success_my_schedue)
        print(res)
        assert res == login_data_success["check"]








