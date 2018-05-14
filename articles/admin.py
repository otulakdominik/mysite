from django.contrib import admin

from .forms import ArticleAdminForm
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm

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


admin.site.register(Article, ArticleAdmin)
