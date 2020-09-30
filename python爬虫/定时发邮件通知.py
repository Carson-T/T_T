# smtplib 用于邮件的发信动作
import smtplib
import schedule
import time
from email.mime.text import MIMEText
from email.header import Header

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = 'tan_biubiu@qq.com'
password = 'igiguiqaynibfgee'

# 收信方邮箱
to_addr = 'tan_biubiu@qq.com'

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
msg = MIMEText('智障','plain','utf-8')

msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header('来自靓仔的问候')

def send_email():
    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server,465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    try:
        server.sendmail(from_addr, to_addr, msg.as_string())
        print("邮件发送成功！")
    except:
        print("邮件发送失败！")
    # 关闭服务器
    server.quit()
def job():
    send_email()

schedule.every(10).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
