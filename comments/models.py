from django.db import models
from blog import models as blog
from articles import models as articles
from django.utils.translation import gettext_lazy as _


class Comments(models.Model):
    body = models.TextField(
        _('body'),
    )

    created = models.DateTimeField(
        _('created'),
        auto_now_add=True,
    )

    entry = models.ForeignKey(
        blog.Entry,
        on_delete=models.CASCADE,
        null=True,
    )

    article = models.ForeignKey(
        articles.Article,
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
