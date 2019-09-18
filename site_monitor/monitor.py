"""Create a script to monitor a site by email notification"""

import os
import smtplib
import requests

USER = os.environ.get('GMAIL_USER')
PASSWORD = os.environ.get('GMAIL_PASS')

print('my email: ', USER)
print('my pass: ', PASSWORD)

r = requests.get('https://www.zooplus.ro', timeout=5)

# if r.status_code != 200:
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(USER, PASSWORD)

    subject = "SITE IS DOWN"
    body = "Make sure the server restarted and it is back up"
    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(USER, 'luiza.mihaiuc@gmail.com', msg)


