# coding=utf-8
import time, os, unittest
from HTMLTestRunner import HTMLTestRunner


class TestRunner(object):
    ''' Run test '''

    def __init__(self, title=u'自动化测试报告', description=u'环境：windows 7'):
        self.work_space = os.path.abspath('.') + '\Test_resourse\\'
        self.cases_path = self.work_space + 'cases\\'
        self.report_path = self.work_space + 'reports\\'
        self.title = title
        self.des = description

    def run(self):

        for filename in os.listdir(self.work_space):
            if filename == "reports":
                break
        else:
            os.mkdir(self.report_path)

        now = time.strftime("%Y%m%d_%H%M%S")
        fp = open(self.report_path + now + "result.html", 'wb')
        tests = unittest.defaultTestLoader.discover(self.cases_path, pattern='test_*.py', top_level_dir=None)
        runner = HTMLTestRunner(stream=fp, title=self.title, description=self.des)
        runner.run(tests)
        fp.close()

    def debug(self):
        tests = unittest.defaultTestLoader.discover(self.cases_path, pattern='test_*.py', top_level_dir=None)
        runner = unittest.TextTestRunner()
        runner.run(tests)


if __name__ == '__main__':
    test = TestRunner()
    test.run()