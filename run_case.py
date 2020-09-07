# -*- coding: utf-8 -*-
import unittest
import time
import HTMLTestRunner
from config import BASE_PATH
import os


def run_case():
    # 测试用例目录
    all_case_list = BASE_PATH + os.sep + "test_case"

    # discover方法定义
    discover = unittest.defaultTestLoader.discover(
        all_case_list,
        pattern="case_*.py",
        top_level_dir=None)

    # 获取时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S")

    # 定义报告存放路径
    file_path = BASE_PATH + os.sep + "report" + os.sep + now + "_report.html"

    fn = open(file_path, "wb")

    # 执行测试套件
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fn,
        title=u"测试报告",
        description=u"用例执行情况"
    )

    runner.run(discover)


if __name__ == '__main__':
    run_case()
