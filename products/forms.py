from django import forms
from django.core.exceptions import ValidationError

from products.models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'description', 'image']
        widgets = {
            'price': forms.NumberInput(attrs={
                'min': '0',
                'step': '0.01',
                'required': True,
                'class': 'form-control'
            }),
        }

    def clean_price(self):
        price = self.cleaned_data['price']
        if price is None or price <= 0:
            raise ValidationError("Цена должна быть положительной.")
        return price