# -*- coding:utf-8 -*-
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.header import Header
import time, hmac, hashlib, base64
import requests
def sendmail(str):
    username = 'no-reply@fzwtest.vip'
    # 发件人密码，通过控制台创建的发件人密码
    password = 'XFFjjd33g95dghs'    #XFFjjd33g95dghs
    # 收件人地址或是地址列表，支持多个收件人，最多30个
    rcptto = '420344291@qq.com'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = Header('BTMX-USDT'.decode('utf-8')).encode()
    msg['From'] = '%s <%s>' % (Header('price'.decode('utf-8')).encode(), username)
    msg['To'] = rcptto
    msg['Message-id'] = email.utils.make_msgid()
    msg['Date'] = email.utils.formatdate()
    # 构建alternative的text/plain部分
    textplain = MIMEText(str, _subtype='plain', _charset='UTF-8')
    msg.attach(textplain)
    # 构建alternative的text/html部分
    texthtml = MIMEText(str, _subtype='html', _charset='UTF-8')
    msg.attach(texthtml)
    try:
        # client = smtplib.SMTP()
        # python 2.7以上版本，若需要使用SSL，可以这样创建client
        client = smtplib.SMTP_SSL()
        # SMTP普通端口为25或80
        client.connect('smtpdm.aliyun.com', 465)
        # 开启DEBUG模式
        client.set_debuglevel(1)
        client.login(username, password)
        # 发件人和认证地址必须一致
        # 备注：若想取到DATA命令返回值,可参考smtplib的sendmaili封装方法:
        #      使用SMTP.mail/SMTP.rcpt/SMTP.data方法
        client.sendmail(username, rcptto, msg.as_string())
        client.quit()
        print '邮件发送成功！'
    except smtplib.SMTPConnectError, e:
        print '邮件发送失败，连接失败:', e.smtp_code, e.smtp_error
    except smtplib.SMTPAuthenticationError, e:
        print '邮件发送失败，认证错误:', e.smtp_code, e.smtp_error
    except smtplib.SMTPSenderRefused, e:
        print '邮件发送失败，发件人被拒绝:', e.smtp_code, e.smtp_error
    except smtplib.SMTPRecipientsRefused, e:
        print '邮件发送失败，收件人被拒绝:', e.smtp_code, e.smtp_error
    except smtplib.SMTPDataError, e:
        print '邮件发送失败，数据接收拒绝:', e.smtp_code, e.smtp_error
    except smtplib.SMTPException, e:
        print '邮件发送失败, ', e.message
    except Exception, e:
        print '邮件发送异常, ', str(e)
if __name__ == '__main__':
    api_path  = "user/info"
    api_key   = "ff5OzGxe3VEgR9pDSLJvp4RheC7KJXeS"
    sec_key   = "Kf3Q7iwxxZQyyc7kaa6U2z9ED4ephEDfX89TXdhFMKaWbAm6n7Bm67YQGaWIX3oH"
    timestamp = int(round(time.time() * 1e3)) # 1562952827927
    message = bytes("{timestamp}+{api_path}")
    secret = bytes(sec_key)
    signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
    header = {'signature':signature}
    res=requests.get(url='https://btmx.com/api/v1/trades?symbol=BTMX-USDT',headers=header)
    a=0
    myalert=0.09
    for i in res.text.split("{\""):
        for j in i.split(","):
            if "p\"" in j:
                a=j[4:10]
        if a!=0 and float(a) < float(myalert):
            # sendmail(a)
            print (a)
            break