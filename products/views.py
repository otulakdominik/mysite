from django.views.generic import (
    ListView,
    DetailView,
    View,
)

from django.shortcuts import (
    redirect,
    render,
)

from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    paginate_by = 10
    queryset = Product.objects.all()
