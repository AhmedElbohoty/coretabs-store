from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from .models import Product

# Create your views here.


def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
