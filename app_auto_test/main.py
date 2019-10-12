#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: LILIANG
# @Date  : 2019/9/16
# @Desc  :  test

import pytest

pytest.main(["-s","-v","-m","smoke","--reruns","2","--reruns-delay","5","--alluredir=outputs//reports"])

#注意：--alluredir= 后面直接跟outputs，而不是/outputs

#allure serve outputs\allure_reports
