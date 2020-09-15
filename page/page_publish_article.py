# -*- coding: utf-8 -*-
'''
相关功能：相关页面元素操作
'''
from base.base import Base
import page


class PagePublishArticle:
    # 初始化
    def __init__(self, driver):
        self.base = Base(driver)

    # 点击内容管理
    def page_click_content_manage(self):
        return self.base.find_xpath(page.tt_content_manage).click()

    # 点击发布文章
    def page_click_publish_article(self):
        return self.base.find_xpath(page.tt_publish_article).click()

    # 输入标题
    def page_input_title(self, title):
        return self.base.find_css(page.tt_title).send_keys(title)

    # 输入内容
    def page_input_content(self, content):
        return self.base.find_xpath(page.tt_content).send_keys(content)

    # 点击自动
    def page_click_cover(self):
        return self.base.find_xpath(page.tt_cover).click()

    # 选择频道
    def page_click_channel_1(self):
        return self.base.find_css(page.tt_channel_1).click()

    def page_click_channel_2(self):
        return self.base.find_xpath(page.tt_channel_2).click()

    # 点击发表
    def page_click_publish(self):
        return self.base.find_xpath(page.tt_publish).click()
