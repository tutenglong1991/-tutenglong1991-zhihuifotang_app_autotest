#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium import webdriver


class TestConnectDevices:

    def setup(self):
        # android应用启动配置
        caps = {"platformName": "android",
                "deviceName": "127.0.0.1:62001",
                "appPackage": "com.atkjsz.smartcemetery",
                "appActivity": "io.dcloud.PandoraEntryActivity",
                "onRest": True
                }
        # ios应用启动配置
        # caps = {
        #     "platformName": "ios",
        #     "platformVersion": "14.5",
        #     "deviceName": "iPhone 8",
        #     "app": "绝对路径"
        # }
        print(caps)
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        driver.implicitly_wait(3)

    def teardown(self):
        pass


if __name__ == "__main__":
    TestConnectDevices().setup()