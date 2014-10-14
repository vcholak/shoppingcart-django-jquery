from django.shortcuts import redirect
from django.http import HttpResponse
#from sports.models import Product

# Create your views here.


# not reachable
def home(request):
    return HttpResponse('<html><title>Sport Products App</title></html>')
    #return redirect('/index.html')


def products():
    all_products = Product.all()
    return all_products


def add_product(name, description, category, price):
    product = Product(name, description, category, price)
    product_id = product.add()
    return product_id

