from django.db.models import Sum, Count, Avg, Min, Max
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .forms import CategoryForm, ProductForm
from .models import Product, Category


class CategoryListView(ListView):
    """
    Отображение списка категорий
    """
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView):
    """
    Создание новой категории
    """
    model = Category
    form_class = CategoryForm
    template_name = 'products/category_form.html'
    success_url = reverse_lazy('products:category_list')


class CategoryUpdateView(UpdateView):
    """
    Редактирование существующей категории
    """
    model = Category
    form_class = CategoryForm
    template_name = 'products/category_form.html'
    success_url = reverse_lazy('products:category_list')


class CategoryDeleteView(DeleteView):
    """
    Удаление категории
    """
    model = Category
    template_name = 'products/category_confirm_delete.html'
    success_url = reverse_lazy('products:category_list')



class ProductListView(ListView):
    """
    Список товаров
    """
    
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        price_min = self.request.GET.get('price_min')
        price_max = self.request.GET.get('price_max')

        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_category'] = self.request.GET.get('category', '')
        context['price_min'] = self.request.GET.get('price_min', '')
        context['price_max'] = self.request.GET.get('price_max', '')
        return context
    
class ProductDetailView(DetailView):
    """
    Детальная страница товара
    """
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"

class ProductCreateView(CreateView):
    """
    Создание нового товара
    """

    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:product_list')


class ProductUpdateView(UpdateView):
    """
    Редактирование существующего товара
    """
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('products:product_list')


class ProductDeleteView(DeleteView):
    """
    Удаление товара
    """
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('products:product_list')
    
class ProductAnalyticsView(TemplateView):
    """
    Аналитика по товарам и категориям
    """
    template_name = 'products/product_analytics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Общая стоимость всех товаров
        context['total_price'] = Product.objects.aggregate(Sum('price'))['price__sum'] or 0

        # Кол-во товаров в каждой категории
        context['category_counts'] = Category.objects.annotate(product_count=Count('products'))

        # Статистика по ценам для каждой категории
        context['category_price_stats'] = Category.objects.annotate(
            avg_price=Avg('products__price'),
            min_price=Min('products__price'),
            max_price=Max('products__price'),
            total_price=Sum('products__price'),
        )

        return context
