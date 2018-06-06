from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings


@shared_task
def send_email(text, receiver):
    subject = 'order'
    msg = EmailMessage(subject, text, settings.ADMIN_EMAIL, [receiver])
    msg.content_subtype = 'html'
    msg.send()
