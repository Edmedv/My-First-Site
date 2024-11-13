from django import forms

from mainapp.models import Product


class CreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'type', 'price', 'photo']

