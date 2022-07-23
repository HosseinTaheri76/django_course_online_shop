from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.utils.translation import gettext as _

from .models import Product
from .forms import CommentForm


def test_translation(request):
    result = _('Hello')
    return HttpResponse(result)


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'
    template_name = 'products/product_list.html'


class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CommentForm
    http_method_names = ['post']

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs.get('product_id'))
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.product = product
        return super().form_valid(form)
