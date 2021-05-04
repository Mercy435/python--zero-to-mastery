'''
# sending email to one person
import smtplib
from email.message import EmailMessage

email = EmailMessage()  # object from emailmessage class
email['from'] = 'Isaac Mercy'
email['to'] = 'Kelvinator4leo@gmail.com'
email['subject'] = 'You won my heart!'

email.set_content('I am a python Master!')

# creating an email server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # an encryption mechanism, to connect to the server
    smtp.login('triumphisaac435@gmail.com', 'python2021')  # email and password to login
    smtp.send_message(email)
    print('all good boss!')
'''

# sending to multiple people

import smtplib
from email.message import EmailMessage
# string template is used to substitute variables inside text using $
from string import Template
# to access html and convert it to text and read with template
from pathlib import Path  # or use the os.path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Isaac Mercy'
email['to'] = 'mercyisaac435@gmail.com'
email['subject'] = 'You won my heart!'

email.set_content(html.substitute(name='TinTin'), 'html') # putting thr html sends the email as a text
# note it can take multiple parameters html.substitute(kwarg) or html.substitute({'name':'TinTin', 'age': 15.....'
# creating an email server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()  # an encryption mechanism, to connect to the server
    smtp.login('triumphisaac435@gmail.com', 'python2021')  # email and password to login
    smtp.send_message(email)
    print('all good boss!')
