from django.views.generic import (
    ListView,
    DetailView,
    View,
)
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/list.html'
    context_object_name = 'articles'
    paginate_by = 10
    queryset = Article.published.all()


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/details.html'
    context_object_name = 'article'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('comments_set')
