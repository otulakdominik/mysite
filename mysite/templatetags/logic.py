from django import template
from django.conf import settings
import hashlib

register = template.Library()


@register.filter()
def hash(type, id):
    items = type + ':' + id + ':' + settings.ADMIN_HASH_SECRET
    hash = hashlib.md5()
    hash.update(items.encode('utf-8'))
    print(hash.hexdigest().upper())
    return hash.hexdigest().upper()
