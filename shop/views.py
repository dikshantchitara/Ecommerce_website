from django.http import HttpResponse
from django.shortcuts import render
from .models  import Product,Contact
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
    return render(request,"shop/aboutus.html")

 
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/Contactus.html')


def tracker(request):
    return render(request,"shop/tracker.html")

def productview(request,myid):
    product = Product.objects.filter(id=myid)
    return render(request,"shop/prodview.html" , {'product':product[0]})

def checkout(request):
    return render(request,"shop/checkout.html")

def search(request):
    return render(request,"shop/search.html")
 