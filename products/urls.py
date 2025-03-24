from django.urls import path
from .views import ProductListView, ProductDetailView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'products'

# Список товаров
urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]

# Добавляем возможность отображения изображений
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)