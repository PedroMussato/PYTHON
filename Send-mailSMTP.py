import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(login_email, password_email, smtp_server, smtp_port, to, subject):
    """
    Function to send an email using the SMTP protocol.

    Parameters:
    - login_email (str): Sender's email address.
    - password_email (str): Sender's password.
    - smtp_server (str): SMTP server for email sending.
    - smtp_port (int): SMTP server port.
    - to (str): Recipient's email address.
    - subject (str): Email subject.
    """
    # Construct the message
    msg = MIMEMultipart()
    msg['From'] = login_email
    msg['To'] = to
    msg['Subject'] = subject
    body = "<html><p>Email body</p></html>"
    msg.attach(MIMEText(body, 'html'))

    # Connect to the server
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(login_email, password_email)
    text = msg.as_string()
    server.sendmail(login_email, to, text)
    server.quit()

# Example usage:
login_email = 'your_email'
password_email = 'your_password'
smtp_server = 'smtp_server'
smtp_port = 465
to = 'recipient_email'
subject = 'Email subject'

sendEmail(login_email, password_email, smtp_server, smtp_port, to, subject)