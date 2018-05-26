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
