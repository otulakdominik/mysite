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

    created = models.DateTimeField(
        'created',
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        'modified',
        auto_now=True,
    )

    pub_date = models.DateTimeField(
        'published data',
        null=True,
        blank=True,

    )

    comments_count = models.PositiveSmallIntegerField(
        'comments count',
        default=0,
        editable=True,
    )

    is_public = models.BooleanField(
        'is public',
        default=False,
    )

    published = PublishedManager()

    class Meta:
        verbose_name = 'entry'
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return self.title
