# multiple mail sender 
Tool to send mail to multiple receivers at a time. "To" will be sender and "Cc" will  be receiver **NOT** Bcc
 
python 2.7
### Tech
Set senders credientials here
  - sendMail.py - source code file
   
    fromaddr = 'user@gmail.com'
    passwd='userpasswd'
    filename = 'complete/path/of/file'
    subject='subject'
    body ='cover_letter_contents' cover_letter should be like this

### Other
  - attatchment.pdf - demo attachment file
  - receivers.txt - list of mail ids each in new line
  - content.txt - mail content file

### run
```sh
$ cd sendMultipleMail
$ python sendMail.py
```

if you get this below error, go to this url 'https://www.google.com/settings/security/lesssecureapps' and allow 'turn on'



Traceback (most recent call last):
  File "s1.py", line 22, in <module>
    server.login(fromaddr, passwd)
  File "/usr/lib/python2.7/smtplib.py", line 622, in login
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (534, '5.7.14 <https://accounts.google.com/ContinueSignIn?sarp=1&scc=1&plt=AKgnsbvrC\n5.7.14 MMlDS9Ohj6nW617lOCMnHuO-RVZTF0wjYRxovQKNVEcKb52PDAN0sjWqZqOdc5X9Yk78ig\n5.7.14 UzzXnrks0nSg6YopVz-sIGSP0K9GvdUECQsO8LoMFBX3B3Ob443u1SGaJTIjxDMrmPFNE3\n5.7.14 tIL4u4pv3FXxSkp8CWw36NlHu-kDkIYMfhNuwkNXYkS_6bI-z1FCjNBFz4P_oQV8DsKnsl\n5.7.14 BH8DWIvLtr1XtuOZT6zamY2z8YRM> Please log in via your web browser and\n5.7.14 then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 y87sm42209250pfi.84 - gsmtp')




### Todos

 - Yes, need to improve

License
----

MIT
