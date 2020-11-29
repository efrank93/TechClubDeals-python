from django.shortcuts import render
from products.models import Product
import requests
from bs4 import BeautifulSoup


def product_index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product_index.html', context)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)

def create_product(request):
    URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, 'html.parser')

    