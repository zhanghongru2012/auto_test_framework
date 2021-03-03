# coding=utf-8
import time, os, unittest
from HTMLTestRunner import HTMLTestRunner


class TestRunner(object):
    ''' Run test '''

    def __init__(self, title=u'自动化测试报告', description=u'环境：windows 10'):
        self.work_space = os.path.abspath('.') + '\TestCases\\'
        # 招远智慧公路
        self.ui_cases_path_baidu = self.work_space + 'UICases\\case_baidu_index\\'
        self.report_path = self.work_space + 'reports\\'
        self.title = title
        self.des = description

    def run_ui(self):

        for filename in os.listdir(self.work_space):
            if filename == "reports":
                break
        else:
            os.mkdir(self.report_path)

        now = time.strftime("%Y%m%d_%H%M%S")
        fp = open(self.report_path + now + "ui_result.html", 'wb')
        # ui自动化路径
        ui_tests = unittest.defaultTestLoader.discover(self.ui_cases_path_baidu, pattern='test_*.py', top_level_dir=None)
        runner = HTMLTestRunner(stream=fp, title=self.title, description=self.des)
        # ui自动化执行
        runner.run(ui_tests)
        fp.close()

    def run_api(self):

        for filename in os.listdir(self.work_space):
            if filename == "reports":
                break
        else:
            os.mkdir(self.report_path)

        now = time.strftime("%Y%m%d_%H%M%S")
        fp = open(self.report_path + now + "api_result.html", 'wb')
        # api自动化路径
        api_tests = unittest.defaultTestLoader.discover(self.ui_cases_path_baidu, pattern='test_highway_*.py', top_level_dir=None)
        runner = HTMLTestRunner(stream=fp, title=self.title, description=self.des)
        # api自动化执行
        runner.run(api_tests)

        fp.close()

    def debug(self):
        tests = unittest.defaultTestLoader.discover(self.ui_cases_path_baidu, pattern='test_*.py', top_level_dir=None)
        runner = unittest.TextTestRunner()
        runner.run(tests)


if __name__ == '__main__':
    test = TestRunner()
    test.run_ui()
    # test.run_api()
