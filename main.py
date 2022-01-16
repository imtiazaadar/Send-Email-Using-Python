# Name : Imtiaz Adar
# Project : Email
# Language Used : Python
# Date : 16/01/2022

import smtplib, os
from email.message import EmailMessage


# send mail
def send_email(email_address, password, receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login(f'{email_address}', f'{password}')
        mail = EmailMessage()
        mail['From'] = email_address
        mail['To'] = receiver
        mail['Subject'] = subject
        mail.set_content(message)
        server.send_message(mail)
        print('\nEMAIL SENT SUCCESSFULLY !!!')
        os.system('pause')
    except Exception:
        print('[INVALID EMAIL OR PASSWORD] OR [PLEASE TURN ON ACCESS OF LESS SECURE APPS] !!!')
        os.system('pause')


# driver
if __name__ == "__main__":
    print('USER EMAIL : ')
    email = input()
    print()
    print('USER PASSWORD : ')
    password = input()
    print()
    print('RECEIVER : ')
    receiver = input()
    print()
    print('SUBJECT : ')
    subject = input()
    print()
    print('MESSAGE : ')
    message = input()
    print()
    print('SENDING !!!')
    send_email(email, password, receiver, subject, message)