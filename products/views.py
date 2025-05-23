from django.shortcuts import render, get_object_or_404, redirect

from .forms import CategoryForm
from .models import Product, Category
from django.views.generic import ListView, DetailView


def category_list(request):
    categories = Category.objects.all()
    return render(request, "products/category_list.html", {"categories": categories})

def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products:category_list")
    else:
        form = CategoryForm()
    return render(request, "products/category_form.html", {"form": form})

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("products:category_list")
    else:
        form = CategoryForm(instance=category)
    return render(request, "products/category_form.html", {"form": form})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect("products:category_list")


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
