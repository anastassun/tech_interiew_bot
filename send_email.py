import settings
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders
from platform import python_version

def email_scripts(result_anketa):
        server = settings.SERVER_MAIL
        user = settings.LOGIN_MAIL
        password = settings.PASSWORD_MAIL

        recipients = settings.SEND_MAIL
        sender = settings.LOGIN_MAIL
        
        subject = f"Кандидат: {result_anketa['name']}"
        text = f"Кандидат: {result_anketa['name']}, должность: {result_anketa['slot']}"
        html = '<html><head></head><body><p>'+text+'</p></body></html>'
    
        filepath = f"userfile/{result_anketa['userfile']}"
        basename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)
        
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = 'BOT tech interview <' + sender + '>'
        msg['To'] = recipients
        msg['Reply-To'] = sender
        msg['Return-Path'] = sender
        msg['X-Mailer'] = 'Python/'+(python_version())

        part_text = MIMEText(text, 'plain')
        part_html = MIMEText(html, 'html')

        open_file = open(filepath,"rb")
        part_file = MIMEApplication(open_file.read(),
                        Name=basename,_subtype="docx")
        
        part_file.add_header('Content-Disposition', f'attachment; filename="{basename}"; size={filesize}')
        encoders.encode_base64(part_file)

        msg.attach(part_text)
        msg.attach(part_html)
        msg.attach(part_file)

        mail = smtplib.SMTP_SSL(server)
        mail.login(user, password)
        mail.sendmail(sender, recipients, msg.as_string())
        mail.quit()

