
import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'xyz@gmail.com'
password = '***************'
sender = 'abc@gmail.com.'
targets = ['abc@gmail.com']

msg = MIMEText('Hi, Python')
msg['Subject'] = 'Data Science is highest paying job'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()
