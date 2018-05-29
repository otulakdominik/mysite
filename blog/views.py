from django.views.generic import (
    ListView,
    DetailView,
    View,
)
from .tasks import comment_count
from comments.forms import CommentForm
from django.shortcuts import get_object_or_404

from django.shortcuts import (
    redirect,
    render,
)

from django.urls import reverse
from .models import Entry


class EntryListView(ListView):
    model = Entry
    template_name = 'blog/list.html'
    context_object_name = 'entries'
    paginate_by = 10
    queryset = Entry.published.all()


class EntryDetailView(DetailView):
    model = Entry
    template_name = 'blog/details.html'
    context_object_name = 'entry'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('comments_set')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, slug):
        entry = get_object_or_404(Entry, slug=slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.entry = entry
            comments.save()
            comment_count.delay(entry.id)
            return redirect(
                reverse('entry:details', kwargs={'slug': slug})
            )
