from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def send_email(text, reciver):
    print(reciver)
    subject = 'order'
    msg = EmailMessage(subject, text, 'products@admin.pl', [reciver])
    msg.content_subtype = 'html'
    msg.send()
