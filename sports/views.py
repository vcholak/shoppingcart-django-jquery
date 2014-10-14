from django.shortcuts import redirect
from django import HttpResponse
#from sports.models import Product

# Create your views here.


# not reachable
def home(request):
    return HttpResponse()
    #return redirect('/index.html')


def products():
    all_products = Product.all()
    return all_products


def add_product(name, description, category, price):
    product = Product(name, description, category, price)
    product_id = product.add()
    return product_id

