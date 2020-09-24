from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import F

from products.models import Product

# Create your views here.


def product(request, id):
    product = Product.objects.filter(id=id)[0]
    print(product)
    return render(request, 'product.html', {'product': product})
