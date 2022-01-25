import smtplib
from email.message import EmailMessage

def email_alert(to, subject, body):
    msg = EmailMessage()

    msg.set_content(body)
    msg["to"] =  to
    user = "jonatan.pretelt@gmail.com"
    msg["from"] = user
    password = "szrorfpusysfkmni"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

if __name__ == '__main__':
    pass
   # email_alert("2012201124@txt.att.net","test", "This is a test sms")
    # email_alert("8138171993@vtext.com", "Love You", "Hi Baby Love you")
