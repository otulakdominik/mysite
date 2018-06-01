from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(
        _('title'),
        max_length=255,
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.name
