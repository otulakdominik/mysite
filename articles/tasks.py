from celery import shared_task
from django.db.models import F
from .models import Article


@shared_task
def comment_count(id):
    article = Article.published.filter(id=id)
    article.update(comments_count=F('comments_count') + 1)
