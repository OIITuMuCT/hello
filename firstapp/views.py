import datetime
from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
    HttpResponseBadRequest,
    HttpResponseForbidden,
)

from .forms import UserForm, UserWForm

# Create your views here.


def contact(request):
    return render(request, 'firstapp/contact.html')


def about(request):
    return render(request, 'firstapp/about.html')


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
    my_text = "Изучаем формы Django"
    context = {"my_text": my_text}
    return render(request, "firstapp/index.html", context)

def my_form(request):
    my_form = UserForm()
    if request.method == "POST":
        my_form = UserForm(request.POST)
        if my_form.is_valid():
            name = my_form.cleaned_data['name']
            return HttpResponse(
                "<h2>Имя введено корректно {0}</h2>".format(name)
            )
    context = {"form": my_form}
    return render(request, "firstapp/my_form.html", context)

def my_form2(request):
    userwform = UserWForm()
    if request.method == "POST":
        userwform = UserWForm(request.POST)
        if userwform.is_valid():
            name = request.POST.get("name" ) # Получить значения поля Имя
            age = request.POST.get("age")  # Получить значения поля Возраст
            output = "<h2>Пользователь</h2><h3>Имя - {0}, \
                Возраст - {1}</h3>".format(name, age)
            return HttpResponse(output)

    context = {"form": userwform}
    return render(request, "firstapp//my_form2.html", context)

def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    if age > 17:
        return HttpResponse("Доступ разрешен")
    else:
        return HttpResponseForbidden("Доступ заблокирован: не достаточно лет")
