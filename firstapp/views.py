from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def contact(request):
    return HttpResponse("Contacts")

def about(request):
    return HttpResponse("About")

def products(request, product_id=1):
    output = "<h2>Product # {0} </h2>".format(product_id)
    return HttpResponse(output)

def users(request, id=1, name="Anonymous"):
    output = "<h2>User: </h2><h3>id: {0} Name: {1}</h3>".format(id, name)
    return HttpResponse(output)

def index(request):
    return HttpResponse('<h1>Main Page</h1>')