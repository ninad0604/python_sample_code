import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

mail_from = ""
mail_to = ""
mail_cc = ""


def send_pdfs_via_email(files_to_attached):
    msg= MIMEMultipart()
    msg['From']= mail_from
    msg['To']= mail_to
    msg['Cc']=mail_cc
    msg['Subject']= "Test Email"
    body = "Please find attached documents. Thank you!!"

    for file in files_to_attached:
        fp = open(file,'rb')
        attach = MIMEApplication(fp.read(),'pdf')
        fp.close()
        attach.add_header("Content-Disposition", 'attachment',filename= file)
        msg.attach(attach)

    msg.attach(MIMEText(body,"plain"))
    server= smtplib.SMTP('SMTP')
    server.send_message(msg)