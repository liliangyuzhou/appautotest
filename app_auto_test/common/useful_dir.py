#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : useful_dir.py
# @Author: LILIANG
# @Date  : 2019/9/16
# @Desc  :  test

import os

#项目目录根路径
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)

#公用目录路径
common_dir=os.path.join(base_dir,'common')
print(common_dir)

#yaml初始化信息路径
caps_dir=os.path.join(base_dir,'desire_caps')
print(caps_dir)

#项目文件输出路径

#项目文件截图输出路径
output_screenshoots_dir=os.path.join(base_dir, 'outputs', 'screenshoots')
print(output_screenshoots_dir)

#项目文件日志输出路径
output_logs_dir=os.path.join(base_dir,'outputs','logs')
print(output_logs_dir)

#项目文件测试报告输出路径
output_report_dir=os.path.join(base_dir,'outputs','reports')
print(output_report_dir)

#元素定位层路径
page_loctors_dir=os.path.join(base_dir,'page_locators')
print(page_loctors_dir)

#页面对象层路径
page_objects_dir=os.path.join(base_dir,'page_objects')
print(page_objects_dir)

#测试用例层路径
testcases_dir=os.path.join(base_dir,'testcases')
print(testcases_dir)

#测试数据层路径
testdatas_dir=os.path.join(base_dir,'testdatas')
print(testdatas_dir)