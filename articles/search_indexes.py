from haystack import indexes
from .models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    title = indexes.CharField(
        document=True,
        use_template=True,
    )

    body = indexes.TextField(
        model_attr='body',
    )

    created = indexes.DateTimeField(
        model_attr='created',
    )

    modified = indexes.DateTimeField(
        model_attr='modified',
    )

    pub_date = indexes.DateTimeField(
        model_attr='pub_date',
    )

    comments_count = indexes.PositiveSmallIntegerField(
        model_attr='comments_count',
    )

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().published
