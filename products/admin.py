from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')  # Поля, которые будут отображаться в списке
    search_fields = ('name', 'description')  # Поля для поиска
    list_filter = ('created_at',)  # Фильтр по дате создания
