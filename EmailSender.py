from email.message import EmailMessage
import ssl
import smtplib
import re

email_sender = 'dsarken666@gmail.com'
# Insert your own password here by generating one via your google account
email_password = ''
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


email_receiver = input('Enter the email of the user to send to: ')

if (re.search(regex, email_receiver)):
    print("Valid Email")
else:
    print("Invalid Email")
    exit(1)

subject = input("Enter a subject: ")
print("")

print("Enter message you wish to send: ")
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
body = '\n'.join(lines)

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
