from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
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


admin.site.register(Article, ArticleAdmin)
