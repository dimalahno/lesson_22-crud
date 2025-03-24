from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    """
        Список товаров
    """
    
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"
    
class ProductDetailView(DetailView):
    """
        Детальная страница товара
    """
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"
