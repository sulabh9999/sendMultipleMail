# -*- coding: utf-8 -*-
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = 'user@mail.com'
passwd='userpasswd'
filename = "attechments.pdf"
subject='my subjact'
body = "containts to send."

attachment = open(filename, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
#server.starttls()
server.login(fromaddr, passwd)


c=0
with open('target_emails') as f:
    content = f.read().split(',')
    for email in content:
       toaddr = email.strip(', \n < >')
       c=c+1
       print '%d--%s'%(c,toaddr)
       msg = MIMEMultipart()
       msg['From'] = fromaddr
       msg['To'] = toaddr
       msg['Subject'] = subject
       
       msg.attach(MIMEText(body, 'plain'))
       msg.attach(part)
       text = msg.as_string()
       server.sendmail(fromaddr, toaddr, text)
       
server.quit()
