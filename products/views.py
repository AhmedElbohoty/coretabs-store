from django.shortcuts import render

from .models import Product

# Create your views here.


def products_list(request):
    products = Product.objects.all()
    context = {'products': products, 'has_products': len(products)}

    return render(request, 'products/products-list.html', context)


def product_details(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        context = {'product': product}
    except:
        context = {'no_product': False}

    return render(request, 'products/product-details.html', context)
