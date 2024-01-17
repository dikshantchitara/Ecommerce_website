from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request , 'shop/index.html')

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
 