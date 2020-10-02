from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import AddProductForm


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}

    return render(request, 'products/products-list.html', context)


def product_details(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        context = {'product': product}
    except:
        context = {'product': False}

    return render(request, 'products/product-details.html', context)


def product_add(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'products/product-add-success.html')

    else:
        form = AddProductForm()

    return render(request, 'products/product-add.html', {'form': form})


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = AddProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return render(request, 'products/product-add-success.html', {'edit': True})

    else:
        form = AddProductForm(instance=product)

    return render(request, 'products/product-add.html', {'form': form, 'edit': True})


def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect("products_list")
