from django.views.generic import (
    ListView,
    DetailView,
    View,
)
from .models import Article
from comments.models import Comments
from comments.forms import CommentForm
from django.shortcuts import get_object_or_404

from django.shortcuts import (
    redirect,
    render,
)
from django.urls import reverse


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.article = article
            comments.save()
            return redirect(
                reverse('article:details', kwargs={'slug': slug})
            )
