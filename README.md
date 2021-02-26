auto_test_framework框架说明：

* 首先请将 TestResources/Tools目录下的 HTMLTestRunner.py先复制到虚拟环境的lib/site-packages目录下
* 然后请下载与自己浏览器版本匹配的chromedriver，下载地址：http://npm.taobao.org/mirrors/chromedriver/

--Base : 封装公共方法

　　1、base_page.py : 包含定义的页面基类，封装常用的页面操作方法

　　2、browser_engine.py : 包含打开浏览器操作以及在相对路径下获取浏览器driver

　　3、logger.py : 日志处理方法

　　4、retry_func.py : 重试 - 装饰器

　　4、send_mail.py : 发送邮件（待完善）

--PageObjects:定义homepage类，用来处理测试常用页面元素及元素操作方法
   
  --1、page_baidu : 被测项目页面集合
      
    --baidu_homepage: 被测页面

--TestCase : 测试用例目录
  
  --ApiCases : 接口测试用例

  --UICases : UI测试用例

--Test_resourse

    --Configs:配置文件存放目录

    --images: 图片存放目录

    --Logs:执行日志以时间格式保存在该文件夹下，如：20200510162812.txt

    --reports:存放执行后生成的测试报告

    --Screenshots:执行截图存放文件，命名格式与日志命名格式一致

    --Tools:浏览器驱动及一些三方库存放文件夹

run_ui.py : UI测试执行文件
run_api.py : 接口测试执行文件



