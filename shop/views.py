from django.http import HttpResponse
from django.shortcuts import render
from .models  import Product
from math import ceil

def Home(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    return render(request, 'shop/index.html', params)

def aboutus(request):
    return HttpResponse("we are at about us")

 
def contact(request):
    return HttpResponse("we are at contact us")

def tracker(request):
    return HttpResponse("we are at tracker")

def productview(request):
    return HttpResponse("we are at product view")

def checkout(request):
    return HttpResponse("we are at checkout page")

def search(request):
    return HttpResponse("we are at search field")
 