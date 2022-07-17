from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'
    template_name = 'products/product_list.html'
