# -*- coding: utf-8 -*-
'''
相关功能：相关页面元素操作
'''
from base.base import Base
import page
import time


class PageLogin:
    # 初始化
    def __init__(self, driver):
        self.base = Base(driver)

    # 输入用户名
    def page_input_username(self, username):
        return self.base.find_css(page.tt_username).send_keys(username)

    # 输入验证码
    def page_input_code(self, code):
        return self.base.find_css(page.tt_code).send_keys(code)

    # 点击登录按钮
    def page_click_login_btn(self):
        return self.base.find_xpath(page.tt_login_btn).click()

    # 获取用户名称
    def page_get_user_name(self):
        return self.base.find_xpath(page.tt_user_name).text

    # 执行业务操作
    def page_login(self, username, code):
        self.page_input_username(username)
        self.page_input_code(code)
        time.sleep(1)
        self.page_click_login_btn()
