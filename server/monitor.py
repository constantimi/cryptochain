#import commands
import subprocess
import smtplib, ssl


def send_email(title, body):
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = "kubernetes.cronjob@gmail.com"  # Enter your address
	receiver_email = "stefanbabukov98@gmail.com"  # Enter receiver address
	password = "kubernetes123"
	message = """\
		Subject: {}

		{}""".format(title,body)
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message)

def site_availability(URL):
	response = "curl --connect-timeout 2 {}".format(URL)
	response = subprocess.run(response.split(),stderr=subprocess.PIPE)
	response = str(response)
	print(response)
	if "curl: (28)" in response or "curl: (6)" in response:
		send_email("Problem with your endpoint","The URL - {} is not responding!".format(URL))

site_availability("http://34.95.86.187") 
site_availability("app:31000")
