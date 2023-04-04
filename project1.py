# go over to our gmail acc and setup 2 factor auth
# generate app password
# create a function to send the mail


from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'rahatmaryam0@gmail.com'
email_password = '9419035296'

email_reciever = 'bipen38217@etondy.com'

subject = 'Hey Wassup!!'
body = ''' hello maryam how does it feel this mini project huh?'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())


