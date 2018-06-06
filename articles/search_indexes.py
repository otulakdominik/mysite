from haystack import indexes
from .models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(
        document=True,
        use_template=True,
    )

    pub_date = indexes.DateTimeField(
        model_attr='pub_date',
    )

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        return self.get_model().published.all()
