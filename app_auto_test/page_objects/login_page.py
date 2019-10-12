#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : login_page.py
# @Author: LILIANG
# @Date  : 2019/9/20
# @Desc  :  test


from page_locators import login_locators as lc
from common import basepage
# 登陆
class LoginPage(basepage.BasePage):

    def login_before(self):
        self.button_click(lc.my_lemon_locator,loc_msg="登陆页面_登陆按钮")
        self.button_click(lc.my_image_locator)


    def login(self, user, passwd):
        self.input_text(lc.user_name_loctor, "登陆页面_用户名输入框", user)
        self.input_text(lc.passwd_name_loctor, "登陆页面_密码输入框", passwd)
        self.button_click(lc.login_button_locator, loc_msg="登陆页面_登陆按钮")