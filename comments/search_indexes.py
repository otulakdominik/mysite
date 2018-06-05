from haystack import indexes
from .models import Comments


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(
        document=True,
        use_template=True,
    )

    created = indexes.DateTimeField(
        model_attr='created',
    )
    entry = indexes.MultiValueField()
    article = indexes.MultiValueField()

    content_auto = indexes.EdgeNgramField(model_attr='body')

    def get_model(self):
        return Comments
