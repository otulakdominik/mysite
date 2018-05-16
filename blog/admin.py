from django.contrib import admin

from .models import Entry


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'body',
        'pub_date',
        'comments_count',
    )
    list_filter = (
        'pub_date',
    )
    readonly_fields = (
        'comments_count',
        'created',
        'modified',
    )


admin.site.register(Entry, BlogAdmin)
