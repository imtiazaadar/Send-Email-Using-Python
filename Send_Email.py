##
# Author : Imtiaz Adar
# Project : Sending Email
# Language Used : Python
##
import smtplib, imghdr
from email.message import EmailMessage

class Email:
    server = ''
    def __init__(self, user_email_, user_password_, recipient_type_, recipient_, subject_, message_):
        self.user_email_ = user_email_
        self.user_password_ = user_password_
        self.recipient_type_ = recipient_type_
        self.recipient_ = recipient_
        self.subject_ = subject_
        self.message_ = message_

    def setup_Server(self):
        global server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

    def sendEmail(self):
        global server
        self.setup_Server()
        try:
            print('SENDING...')
            server.login(f'{self.user_email_}', f'{self.user_password_}')
            email = EmailMessage()
            email['From'] = self.user_email_
            recipients = ', '.join(self.recipient_)
            email[f'{self.recipient_type_}'] = recipients
            email['Subject'] = self.subject_
            email.set_content(self.message_)
            server.send_message(email)
            print('# SENT SUCCESSFULLY #')
        except Exception:
            print('# FAILED #')

    def sendAttachment(self, filepath):
        global server
        self.setup_Server()
        try:
            print('SENDING...')
            server.login(f'{self.user_email_}', f'{self.user_password_}')
            email = EmailMessage()
            email['From'] = self.user_email_
            recipients = ', '.join(self.recipient_)
            email[f'{self.recipient_type_}'] = recipients
            email['Subject'] = self.subject_
            email.set_content('IMAGE ATTACHED...')
            with open(filepath, 'rb') as picture:
                file = picture.read()
                file_type = imghdr.what(picture.name)
                file_name = picture.name
            email.add_attachment(file, maintype='image', subtype=file_type, filename=file_name)
            server.send_message(email)
            print('# SENT SUCCESSFULLY #')
        except Exception:
            print('# FAILED #')

if __name__=="__main__":
    print('!! MAIL APPLICATION BY IMTIAZ ADAR !!')
    print("# YOU ARE GONNA BE SENDING EMAIL #")
    print(f'\n')
    user_mail = input('USER EMAIL : ')
    user_pass = input('USER PASSWORD : ')
    recipient_type = input('RECIPIENT TYPE : ')
    recipient = [x for x in input('RECIPIENT : ').split()]
    subject = input('SUBJECT : ')
    message = input('MESSAGE : ')
    email_ = Email(user_mail, user_pass, recipient_type, recipient, subject, message)
    email_.sendEmail()
    email_.sendAttachment(input('ATTACHMENT PATH : '))