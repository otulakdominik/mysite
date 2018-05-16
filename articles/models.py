from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_public_lte=timezone.now())


class Article(models.Model):
    title = models.CharField(
        _('title'),
        max_length=255,
    )

    body = models.TextField(
        _('body'),
    )

    created = models.DateTimeField(
        _('created'),
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        _('modified'),
        auto_now=True,
    )

    pub_date = models.DateTimeField(
        _('published date'),
        null=True,
        blank=True,
    )

    comments_count = models.PositiveSmallIntegerField(
        _('comments count'),
        default=0,
        editable=True,
    )

    is_public = models.BooleanField(
        _('is public'),
        default=False,
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')

    def __str__(self):
        return self.title
