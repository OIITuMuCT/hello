from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect

# Create your views here.

def contact(request):
    return HttpResponseRedirect("/about")
    # return HttpResponse("Contacts")

def about(request):
    return HttpResponse("About")

def products(request, product_id=1):
    category = request.GET.get("cat", "Не задана")
    output = "<h2>Product # {0}  Category: {1} </h2>".format(product_id, category)
    return HttpResponse(output)

def users(request, id=1, name="Anonymous"):
    id = request.GET.get("id", "Не задано")
    name = request.GET.get("name", "Не задано")
    output = "<h2>User: </h2><h3>id: {0} Name: {1}</h3>".format(id, name)
    return HttpResponse(output)

def details(request):
    return HttpResponsePermanentRedirect('/')

def index(request):
    return HttpResponse('<h1>Main Page</h1>')


