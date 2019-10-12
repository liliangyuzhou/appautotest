#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : login_locators.py
# @Author: LILIANG
# @Date  : 2019/9/20
# @Desc  :  test

from appium.webdriver.common.mobileby import MobileBy

#点击我的柠檬
my_lemon_locator=(MobileBy.ID,"com.lemon.lemonban:id/navigation_my")

#点击我的头像
my_image_locator=(MobileBy.ID,"com.lemon.lemonban:id/fragment_my_lemon_avatar_layout")

#用户名输入框
user_name_loctor=(MobileBy.ID,"com.lemon.lemonban:id/et_mobile")

#密码输入框
passwd_name_loctor=(MobileBy.ID,"com.lemon.lemonban:id/et_password")

#登录按钮
login_button_locator=(MobileBy.ID,"com.lemon.lemonban:id/btn_login")

#登录成功后才出现的我的课表

login_success_my_schedue=(MobileBy.ID,'com.lemon.lemonban:id/fragment_my_lemon_expend_title')

# 密码错误的toast
toast_loc = (MobileBy.XPATH, '//*[contains(@text,"错误的账号信息")]')

# 账号密码为空的toast
toast_loc_null = (MobileBy.XPATH, '//*[@text()="手机号码或密码不能为空"]')

