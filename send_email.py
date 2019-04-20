from email.mime.text import MIMEText
import smtplib

def send_email(email, height):
	from_email="email gmail"
	password="mp%"
	to_email=email

	subject="Height Data"
	message = "Bonjour, votre taille est de {}".format(height)

	msg=MIMEText(message, 'html')
	msg["subject"]=subject
	msg["to"]=to_email
	msg['From']=from_email

	gmail=smtplib.SMTP('smtp.gmail.com', 587)
	gmail.ehlo()
	gmail.starttls()
	gmail.login(from_email, password)
	gmail.send_message(msg)

