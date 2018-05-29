from celery import shared_task
from django.db.models import F
from .models import Entry


@shared_task
def comment_count(id):
    entry = Entry.published.filter(id=id)
    entry.update(comments_count=F('comments_count') + 1)
