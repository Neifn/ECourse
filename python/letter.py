#!/usr/bin/env python
# -*-coding: utf8 -*-
import smtplib
from email.mime.text import MIMEText
from email.message import Message
import getpass

me = 'alexandrshahmatov@gmail.com'
you = 'alexshahtranslations@gmail.com'
text = 'hello second email'
subj = 'test letter'

server = "smtp.gmail.com"
port = 25
user_name = "alexandrshahmatov@gmail.com"
# calling for method which allows secure typing your password securly
user_passwd = getpass.getpass("Enter your Password:")

# Add (text, "plain", "utf-8") to send messages not as mime objects
msg = MIMEText(text, "", "utf-8")
msg['Subject'] = subj
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP(server, port)
s.ehlo()
s.starttls()
s.ehlo()
s.login(user_name, user_passwd)
s.sendmail(me, you, msg.as_string())

s.quit

