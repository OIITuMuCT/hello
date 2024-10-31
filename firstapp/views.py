from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
    HttpResponseBadRequest,
    HttpResponseForbidden,
)
from django.template.response import TemplateResponse
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
    return HttpResponsePermanentRedirect("/")


def index(request):
    return TemplateResponse(request, "firstapp/home.html")
    return render(request, "firstapp/home.html")
    return render(request, "index.html")
    return HttpResponse("<h1>Main Page</h1>")


def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    if age > 17:
        return HttpResponse("Доступ разрешен")
    else:
        return HttpResponseForbidden("Доступ заблокирован: не достаточно лет")
