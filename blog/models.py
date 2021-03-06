from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(pub_date__lte=timezone.now())


class Entry(models.Model):
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
        _('published data'),
        null=True,
        blank=True,

    )

    comments_count = models.PositiveSmallIntegerField(
        _('comments count'),
        default=0,
        editable=True,
    )

    slug = models.SlugField(
        _('slug'),
        max_length=255
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = _('entry')
        verbose_name_plural = _('entries')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('entry:details', kwargs={'slug': self.slug})
