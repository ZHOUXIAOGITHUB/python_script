#-*- encoding=utf8 -*-
#Author:
#Time:  2021/9/2 13:59
#File:  test_runner.py
import unittest

from house_dictionary.html_test_runner import HTMLTestRunner


class Test_Runner():
    def test_runner(self):
        test_suite = unittest.TestSuite()
        test_suite.addTests(unittest.defaultTestLoader.discover(
            "E:\\louxun\\python_script\\boss\\house_dictionary", pattern="main_test.py"))
        # 生成报告文件
        # report_file = open("E:\\louxun\\python_script\\boss\\house_dictionary\\lx.html", mode="wb")
        # run_test = HTMLTestRunner(stream=report_file, title="boss自动化报告",
        #                description ="用例" )
        run_test = unittest.TextTestRunner()
        run_test.run(test_suite)

