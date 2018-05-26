from django.views.generic import (
    ListView,
    DetailView,
    View,
)
from .models import Entry


class EntryListView(ListView):
    model = Entry
    template_name = 'blog/list.html'
    context_object_name = 'entries'
    paginate_by = 10
    queryset = Entry.published.all()


class EntryDetailView(DetailView):
    template_name = 'blog/details.html'
    context_object_name = 'entries'
    queryset = Entry.published.all()

    def get_queryset(self):
        return super().get_queryset().prefetch_related('comment')
