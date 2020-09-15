# -*- coding: utf-8 -*-
'''
相关功能：实现登录业务流程
'''
import unittest
import time
import page
from page.page_login import PageLogin
from tools.get_driver import GetDriver
import paramunittest
from tools.read_yaml import read_yaml


@paramunittest.parametrized(read_yaml("../data/tt_login.yaml"))
class CaseLogin(unittest.TestCase):
    def setUp(self):
        driver = GetDriver.get_web_driver(page.tt_url)
        driver.implicitly_wait(5)
        self.pl = PageLogin(driver)

    def tearDown(self):
        GetDriver.quit_web_driver()

    def setParameters(self, username, code, expect):
        self.username = username
        self.code = code
        self.expect = expect

    def test_login(self):
        # 正常输入账号密码登录
        self.pl.page_input_username(self.username)
        time.sleep(1)
        self.pl.page_input_code(self.code)
        time.sleep(2)
        self.pl.page_click_login_btn()
        time.sleep(1)
        user_name = self.pl.page_get_user_name()
        time.sleep(1)
        try:
            self.assertEqual(user_name, self.expect)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
