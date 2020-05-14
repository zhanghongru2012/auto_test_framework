UITestFramework:

--Base

　　1、base_page.py : 包含定义的页面基类，封装常用的页面操作方法

　　2、browser_engine.py : 包含打开浏览器操作以及在相对路径下获取浏览器driver

　　3、logger.py : 日志处理方法

--PageObjects:定义homepage类，用来处理测试常用页面元素及元素操作方法

--Test_resourse

    --cases:测试用例集存放目录

    --Configs:配置文件存放目录

    --Logs:执行日志以时间格式保存在该文件夹下，如：20200510162812.txt

    --Screenshots:执行截图存放文件，命名格式与日志命名格式一致

    --reports:存放执行后生成的测试报告

    --Tools:浏览器驱动及一些三方库存放文件夹

run.py: 测试框架执行入口文件




