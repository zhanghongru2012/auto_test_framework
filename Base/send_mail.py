import smtplib
from email.header import Header
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import email
import base64


class SendMail():
    def __init__(self):
        self.mail_host = "smtp.qq.com"
        self.mail_user = "462228812@qq.com"
        self.mail_password = "dhhvrysmoxzqbjbb"
        self.sender = '462228812@qq.com'  # 发件人邮箱
        self.receivers = ['zhanghongru2012@163.com']  # 收件人邮箱
        self.messages = MIMEText('python邮件测试', 'plain', 'utf-8')  # 邮件正文
        self.messages['From'] = Header('python机器人', 'utf-8')  # 发件人信息
        self.messages['To'] = Header('测试', 'utf-8')  # 收件人信息
        self.messages['Subject'] = Header('Python邮件测试，收到请忽略...', 'utf-8')  # 邮件主题

    def login(self):
        try:
            smtpobj = smtplib.SMTP()
            smtpobj.connect(self.mail_host, 25)
            smtpobj.login(self.mail_user, self.mail_password)
            smtpobj.sendmail(self.sender, self.receivers, self.messages.as_string())
            print('邮件发送成功')
        except smtplib.SMTPException as e:
            print(e)
            print('Error: 无法发送邮件')