from django.views.generic import ListView

from django.shortcuts import (
    redirect,
    render,
    get_object_or_404,
)


from .models import Product
from .forms import CartAddProductForm


class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    paginate_by = 10
    queryset = Product.objects.all()


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug,)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'products/detail.html', context)
