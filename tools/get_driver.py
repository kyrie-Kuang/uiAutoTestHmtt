# -*- coding: utf-8 -*-
'''
相关功能：获取driver
'''
from selenium import webdriver


class GetDriver:
    web_driver = None

    @classmethod
    def get_web_driver(cls, url):
        if cls.web_driver is None:
            cls.web_driver = webdriver.Firefox()
            cls.web_driver.maximize_window()
            cls.web_driver.get(url)
        return cls.web_driver

    @classmethod
    def quit_web_driver(cls):
        if cls.web_driver:
            cls.web_driver.quit()
            cls.web_driver = None
