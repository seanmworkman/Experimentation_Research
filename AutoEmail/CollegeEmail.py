import smtplib, ssl
import os
from dotenv import load_dotenv
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



load_dotenv()

def readCSV():
    emails = []
    with open('./EmailLists/MLBEmail.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        for row in csv_reader:
            emails.append(row)

    return emails

def sendEmails(emails):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "sean.workman.691@gmail.com"  # Enter your address
    password = os.environ.get("GMAIL_PASS")
    

    receiver_email = "sean.workman.691@gmail.com"  # Enter receiver address
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "Team Gear"
    message["From"] = sender_email
    

    for email in emails:
        receiver_email = email[1]
        message["To"] = receiver_email
        # College Email Template
        # text = """\
        # To whom it may concern,\n
        # I am interested in attending %s and would love to represent your school. I'm sure you get these requests all the time 
        # but is there any chance I could get a flag, t-shirt, sweatshirt or really anything you could offer me. If you all 
        # are able to help me out my address is: \n
        # 332 Laskin Road Apt. 321
        # Virginia Beach, VA 23451\n
        # Thank you for your time and I hope to be able to show my school pride soon.\n
        # Sean Workman  
        # """ % email[0]
        # MLB Email Template
        text = """\
        To whom it may concern,\n
        I have been a long time fan of the %s. I'm sure you get requests like this all the time 
        but if you could send me a sweatshirt, t-shirt, flag, or really anything from you or your minor league teams that would mean a lot. I am a men's large.
        If you are able to help me out my address is: \n
        332 Laskin Road Apt. 321
        Virginia Beach, VA 23451\n
        Thank you for your time and I hope to be able to show my team pride soon.\n
        Sean Workman  
        """ % email[0]
        message.attach(MIMEText(text, "plain"))
        print(email[0])
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

emails = readCSV()
print(emails)
sendEmails(emails)