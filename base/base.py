# -*- coding: utf-8 -*-
'''
相关功能：selenium定位方法
'''


class Base:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # xpath定位
    def find_xpath(self, value):
        return self.driver.find_element_by_xpath(value)

    # css定位
    def find_css(self, value):
        return self.driver.find_element_by_css_selector(value)
