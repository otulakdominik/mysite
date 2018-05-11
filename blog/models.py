from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)


class Entry(models.Model):
    title = models.CharField(
        'title',
        max_length=255,
    )

    body = models.TextField(
        'body',
    )

    created = models.DataTimeField(
        'created',
        auto_now_add=True,
    )

    modified = models.DataTimeField(
        'modified',
        auto_now=True,
    )

    pub_data = models.DataTimeField(
        'published data',
        null=True,
        blank=True,

    )

    comments_count = models.PositiveSmallIntegierField(
        'comments count',
        default=0,
        editable=True,
    )

    is_public = models.BooleanField(
        'is public',
        default=False,
    )

    published = PublishedManager()
