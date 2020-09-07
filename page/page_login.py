# -*- coding: utf-8 -*-
'''
相关功能：相关页面元素操作
'''
from base.base import Base
import page


class PageLogin:
    # 初始化
    def __init__(self, driver):
        self.base = Base(driver)

    # 输入用户名
    def page_input_username(self, value):
        return self.base.find_css(page.tt_username).send_keys(value)

    # 输入验证码
    def page_input_code(self, value):
        return self.base.find_css(page.tt_code).send_keys(value)

    # 点击登录按钮
    def page_click_login_btn(self):
        return self.base.find_css(page.tt_login_btn).click()

    # 获取用户名称
    def page_get_user_name(self):
        return self.base.find_xpath(page.tt_user_name).text
