1. it's bunch of files.
   - 'sendmail.py' is master file.
   - 'target_emails' is file with list od many HRs in companys.
   - 'attechments.pdf' is additional file to be sent.
   
2. configuration details ---  
         fromaddr = 'user@gmail.com'
         passwd='userpasswd'
         filename = 'complete/path/of/file'
         subject='subject'
         body ='cover_letter_contents' cover_letter should be like this

"Respected HR Team,\n I am submitting here with my resume for your perusal and favorable consideration for the post of “Software engineer” in your organization.\n Review of my credentials indicates that I am a qualified B.Tech from NATIONAL INSTITUTE OF TECHNOLOGY, possess comprehensive knowledge of C, C++,Data structure, Core java AND Web Designing(intermediate).Literature Survey on Amazon Elastic Compute Cloud(EC2) as my project during academic.\n With exceptional communication and interpersonal skills, my self – confidence, innovative approach and quick adaptability to changing processes and trends have been my biggest assets.\n I am seeking a challenging job that would synergize my skills and experience with the objectives of the organization.\nThe above credentials along with my enclosed resume make me ideally suitable for a position in your organization. I would appreciate an opportunity for a personal interview.\nThanking you in anticipation of a favorable reply.\n\n Yours sincerely\n XYZ"



[if you get this error(given bellow) go to this url 'https://www.google.com/settings/security/lesssecureapps' and allow 'turn on']
Traceback (most recent call last):
  File "s1.py", line 22, in <module>
    server.login(fromaddr, passwd)
  File "/usr/lib/python2.7/smtplib.py", line 622, in login
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (534, '5.7.14 <https://accounts.google.com/ContinueSignIn?sarp=1&scc=1&plt=AKgnsbvrC\n5.7.14 MMlDS9Ohj6nW617lOCMnHuO-RVZTF0wjYRxovQKNVEcKb52PDAN0sjWqZqOdc5X9Yk78ig\n5.7.14 UzzXnrks0nSg6YopVz-sIGSP0K9GvdUECQsO8LoMFBX3B3Ob443u1SGaJTIjxDMrmPFNE3\n5.7.14 tIL4u4pv3FXxSkp8CWw36NlHu-kDkIYMfhNuwkNXYkS_6bI-z1FCjNBFz4P_oQV8DsKnsl\n5.7.14 BH8DWIvLtr1XtuOZT6zamY2z8YRM> Please log in via your web browser and\n5.7.14 then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 y87sm42209250pfi.84 - gsmtp')


