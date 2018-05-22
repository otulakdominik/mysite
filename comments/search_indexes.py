from haystack import indexes
from .models import Comments
import datetime


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    body = indexes.TextField(
        document=True,
        use_template=True,
    )

    created = indexes.DateTimeField(
        model_attr='created',
    )
    entry = indexes.MultiValueField()
    article = indexes.MultiValueField()

    def get_model(self):
        return Comments

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(
            pub_date__lte=datetime.datetime.now()
        )
