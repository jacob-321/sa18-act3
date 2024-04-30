import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Product

def home(request):
    return render(request, 'myapp/index.html')

def product_index(request):
    product_list = Product.objects.all()
    return render(request, 'myapp/index.html', {'products': product_list})

def product_show(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'myapp/show.html', {'product': product})

def product_show(request, id):
    product = Product.objects.all()
    return render(request, 'myapp/show.html', {'product': product})

def product_index(request):
    with open('myapp/fixtures/products.json') as json_file:
        products = json.load(json_file)
    return render(request, 'myapp/show.html', {'products': products})
