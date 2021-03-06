# -*- coding: utf-8 -*-
import smtplib,re,sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = 'myemail@mail.com'#add user email address
passwd='password'            #add email password.
filename = "attechments.pdf" #add your doc here
subject='my subjact'         #add your subject here
emailFile = 'email_file.txt'
coverLetter = 'cover_letter.txt'


def setup_function():
    regex = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')
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
    content = file_to_str(emailFile)   
    body = file_to_str(coverLetter)
    for toaddr in re.findall(regex, content): 
       		c=c+1
       		msg = MIMEMultipart()
       		msg['From'] = fromaddr
       		msg['To'] = toaddr
       		msg['Subject'] = subject
       		msg.attach(MIMEText(body, 'plain'))
       		msg.attach(part)
       		text = msg.as_string()
       		server.sendmail(fromaddr, toaddr, text)
                print '%d--%s'%(c,toaddr)  
    server.quit()


def file_to_str(filename):
    try:
       with open(filename) as f:
         return f.read()#.lower() 
    except IOError:
       print 'file does not exist...->',(filename)
       sys.exit()


if __name__ == '__main__':
     setup_function()
