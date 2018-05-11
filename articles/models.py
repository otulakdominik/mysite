from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)


class Article(models.Model):
    title = models.CharField(
        'title',
        max_length=255,
    )

    body = models.TextField(
        'body',
    )

    created = models.DateField(
        'created',
        auto_now_add=True,
    )

    modified = models.DateField(
        'modified',
        auto_now=True,
    )

    pub_date = models.DateField(
        'published date',
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
