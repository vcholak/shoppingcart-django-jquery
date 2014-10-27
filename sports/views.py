from django.shortcuts import render
from django.http import JsonResponse

from sports.models import Product, Order, OrderItem


def home(request):
    products = Product.all()
    return render(request, 'home.html', {'products': products})


def order(request):
    if request.method == 'POST':
        name = request.POST.get('fname', '')
        city = request.POST.get('city', '')
        street = request.POST.get('street', '')
        postal = request.POST.get('zip', '')
        country = request.POST.get('country', '')
        state = request.POST.get('state', '')
        items = request.POST.get('items', [])

        ord = Order(name=name, city=city, street=street, state=state, postal=postal, country=country)
        ord.save()
        order_no = ord.id

        ord.items = []
        for it in items:
            name = it['name']
            product = Product.objects.get(name=name)
            count = it['count']
            item = OrderItem(count=count, product=product)
            ord.items.append(item)
        ord.save()

        return JsonResponse({"orderNo": order_no})