from django.db import models


class Comments(models.Model):
    body = models.TextField(
        'body',
    )

    created = models.DateField(
        'created',
        auto_now_add=True,
    )
