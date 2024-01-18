from django.http import HttpResponse
from django.shortcuts import render
from .models  import Product
from math import ceil

def Home(request):
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

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
 