import smtplib
import unfollowers
from os import environ


def send_email(unfollower: str):
    send_to = environ['SEND_TO']
    send_from = environ['SEND_FROM']
    send_from_password = environ['SEND_FROM_PASSWORD']

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(send_from, send_from_password)

    subject = f'{unfollower} unfollowed you!'
    body = f'Hey there!\n{unfollower} unfollowed you!'
    message = f'Subject: {subject}\n\n{body}'
    server.sendmail(send_from, send_to, message)
    print(f'Sending e-mail to {send_to}.')

    server.quit()
    unfollowers.main()
