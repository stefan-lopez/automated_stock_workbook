def emailer(message, subject, fileNames, toAddressList, email, email_pass):
    print("Sending email...")
    from smtplib import SMTP_SSL as SMTP #SSL connection
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    from email.mime.base import MIMEBase
    from email import encoders

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = ", ".join(toAddressList)
    msg['Subject'] = subject
    message = str(message)
    msg.attach(MIMEText(message))

    for file in range(0,len(fileNames)):
        # open the file to be sent 
        openAttachment = open(fileNames[file], 'rb')
     
        # instance of MIMEBase and named as p
        attachmentDoc = MIMEBase('application', 'octet-stream')
     
        # To change the payload into encoded form
        attachmentDoc.set_payload((openAttachment).read())
     
        # encode into base64
        encoders.encode_base64(attachmentDoc)
      
        attachmentDoc.add_header('Content-Disposition', "attachment; filename= %s" % fileNames[file])
     
        # attach the instance 'p' to instance 'msg'
        msg.attach(attachmentDoc)

    ServerConnect = False
    try:
        smtp_server = SMTP('smtp.gmail.com','465')
        smtp_server.login(email, email_pass)
        ServerConnect = True
    except:
        print("Authentication failed")

    if ServerConnect == True:
        try:
            smtp_server.sendmail(email, toAddressList, msg.as_string())
            print("Email sent!")
        except SMTPException as e:
            print("Error: unable to send email", e)
        finally:
            smtp_server.close()