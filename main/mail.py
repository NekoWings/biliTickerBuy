import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 加载配置文件
with open('./config.json', 'r') as f:
    config = json.load(f)

def send_mail(msg):
    # Define email addresses and login credentials
    sender_email = "nekowings@outlook.com"
    sender_password = config["email_passwd"]
    receiver_email = "nekowings@outlook.com"

    # Create a multipart message object and set parameters
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Test Email"

    # Add body and attachment to message
    message.attach(MIMEText(msg, "plain"))

    # Create SMTP session and login to account
    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send email and terminate SMTP session
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()