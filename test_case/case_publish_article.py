# -*- coding: utf-8 -*-
'''
相关功能：实现发布文章业务流程
'''
import unittest
import time
import paramunittest
import page
from page.page_login import PageLogin
from tools.get_driver import GetDriver
from tools.read_yaml import read_yaml
from page.page_publish_article import PagePublishArticle


@paramunittest.parametrized(read_yaml("../data/tt_login.yaml"))
class CasePublishArticle(unittest.TestCase):
    def setUp(self):
        self.driver = GetDriver.get_web_driver(page.tt_url)
        self.driver.implicitly_wait(5)
        PageLogin(self.driver).page_login("13812345678", "246810")
        self.ppa = PagePublishArticle(self.driver)

    def tearDown(self):
        GetDriver.quit_web_driver()

    def setParameters(self, title, content):
        self.title = title
        self.content = content

    def test_publish_article(self):
        # 发布文章
        time.sleep(2)
        self.ppa.page_click_content_manage()
        self.ppa.page_click_publish_article()
        time.sleep(1)
        self.ppa.page_input_title(self.title)
        self.driver.switch_to.frame(page.tt_iframe)
        self.ppa.page_input_content(self.content)
        self.driver.switch_to_default_content()
        self.ppa.page_click_cover()
        self.ppa.page_click_channel_1()
        self.ppa.page_click_channel_2()
        self.ppa.page_click_publish()


if __name__ == '__main__':
    unittest.main()
