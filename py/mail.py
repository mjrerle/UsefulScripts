#!/usr/bin/python
import smtplib

sender = 'matterle@live.com'
receivers = 'matterle@live.com'
message = "This is a test email."

try:
    smtpObj = smtplib.SMTP('smtp.live.com')
    smtpObj = sendmail(sender, receivers, message)
    print "Success"
except smtplib.SMTPException:
    print "Error: unable to send email"
    
