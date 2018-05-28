from django.views.generic import (
    ListView,
    DetailView,
    View,
)
from django.shortcuts import get_object_or_404
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
    context_object_name = 'entries'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('comments_set')
