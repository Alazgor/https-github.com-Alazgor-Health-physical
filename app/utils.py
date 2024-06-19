from datetime import datetime
from flask_mail import Message
from app import mail

# Функция для отправки электронной почты
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

# Функции для работы с датами
def format_datetime(date):
    return date.strftime('%Y-%m-%d %H:%M:%S')

def get_current_timestamp():
    return datetime.utcnow()
