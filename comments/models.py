from django.db import models
from blog import models as blog
from articles import models as articles


class Comments(models.Model):
    body = models.TextField(
        'body',
    )

    created = models.DateField(
        'created',
        auto_now_add=True,
    )

    entry = models.ForeignKey(
        blog.Entry,
        on_delete=models.CASCADE,
    )

    article = models.ForeignKey(
        articles.Article,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
