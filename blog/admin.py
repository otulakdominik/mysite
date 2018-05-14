from django.contrib import admin

from .forms import BlogAdminForm
from .models import Entry


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

    list_display = (
        'title',
        'body',
        'pub_date',
        'is_public',
        'comments_count',
    )
    list_editable = (
        'is_public',
    )
    list_filter = (
        'is_public',
    )
    readonly_fields = (
        'comments_count',
        'created',
        'modified',
    )


admin.site.register(Entry, BlogAdmin)
