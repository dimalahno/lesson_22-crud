from django.test import TestCase
from django.urls import reverse
from products.models import Product
from decimal import Decimal
from django.core.files.uploadedfile import SimpleUploadedFile

class ProductViewsTest(TestCase):
    def setUp(self):
        """Создаем тестовые данные перед каждым тестом"""
        self.product = Product.objects.create(
            name="Тестовый товар",
            description="Описание тестового товара",
            price=Decimal("999.99"),
            image=SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg"),
        )

    def test_product_list_view(self):
        """Тестирование списка товаров"""
        # Проверяем URL списка товаров
        response = self.client.get(reverse("products:product_list"))
        self.assertEqual(response.status_code, 200)
        # Проверяем, что товар есть на странице
        self.assertContains(response, "Тестовый товар")  

    def test_product_detail_view(self):
        """Тестирование детальной страницы товара"""
        # Проверяем URL товара
        response = self.client.get(reverse("products:product_detail", args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        # Проверяем описание товара
        self.assertContains(response, "Описание тестового товара")

    def test_product_not_found(self):
        """Тестирование 404 для несуществующего товара"""
        # Несуществующий товар
        response = self.client.get(reverse("products:product_detail", args=[999]))
        self.assertEqual(response.status_code, 404)
