from django.forms import ModelForm, TextInput, Textarea, NumberInput
from .models import Product


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('brand', 'title', 'description', 'price', 'image')
        widgets = {
            'brand': TextInput(attrs={'class': 'form-inp'}),
            'title': TextInput(attrs={'class': 'form-inp'}),
            'description': Textarea(attrs={'class': 'form-textarea'}),
            'price': NumberInput(attrs={'class': 'form-inp', 'min': '0'}),
        }
