from django.db import models
from blog.models import Entry
from articles.models import Article
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
        Entry,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __str__(self):
        return self.body
