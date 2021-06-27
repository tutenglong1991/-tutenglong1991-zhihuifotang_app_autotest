#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver

class TestConnectDevices:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "YCYNW18207003632"
        caps["appPackage"] = "com.atkjsz.smartcemetery"
        caps["appActivity"] = "io.dcloud.PandoraEntryActivity"
        # caps["appPackage"] = "com.tencent.mm"
        # caps["appActivity"] = ".plugin.account.ui.LoginPasswordUI"
        caps["onRest"] = "True" # onRest可避免app数据被重置，如可避免重复弹出登陆更新等弹窗等，可记录登陆状态
        print(caps)
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        driver.implicitly_wait(5)

    def teardown(self):
        pass

if __name__ == "__main__":
    TestConnectDevices().setup()