import datetime
from django.shortcuts import render, redirect
from django.http import (
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseNotFound,
    HttpResponseBadRequest,
    HttpResponseForbidden,
)

from .forms import UserForm, UserWForm, UserCForm, ImageForm
from .models import Person, Image
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
    my_text = "Изучаем модели Django"
    people_kol = Person.object_person.count()
    context = {"my_text": my_text, "people_kol": people_kol}
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

def my_form3(request):
    form = UserCForm()
    if request.method == "POST":
        form = UserCForm(request.POST)
        if form.is_valid():
            person = Person()
            person.name=form.cleaned_data['name']
            person.age=form.cleaned_data['age']
            person.save()
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))
                print("Запись добавлена в базу данных Имя: {0} Возраст: {1}".format(person.name, person.age))
            return redirect('my_form3')
    my_text = 'Сведения о клиентах'
    people = Person.object_person.all()
    form = UserCForm()
    context = {"my_text": my_text, "people": people, "form": form}
    return render(request, 'firstapp/my_form3.html', context)

# Изменение данных о клиенте в БД
def edit_form(request, id):
    person = Person.object_person.get(id=id)
    # Если пользователь вернул отредактированные данные
    if request.method == "POST":
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
        return redirect('my_form3')
    # Если пользователь отправляет данные на редактирование
    data = { "person": person}
    return render(request, "firstapp/edit_form.html", context=data)
# Удаление данны о клиенте из БД
def delete(request, id):
    try:
        person = Person.object_person.get(id=id)
        person.delete()
        return redirect('my_form3')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")

def access(request, age):
    if age not in range(1, 111):
        return HttpResponseBadRequest("Некорректные данные")
    if age > 17:
        return HttpResponse("Доступ разрешен")
    else:
        return HttpResponseForbidden("Доступ заблокирован: не достаточно лет")

def form_up_img(request):

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Форма сохранена успешно!")
    my_text = "Загруженные изображения"
    my_img = Image.obj_img.all()
    form = ImageForm()
    context = {'my_text': my_text, "my_img": my_img, "form": form}
    return render(request, 'firstapp/form_up_img.html', context)

def delete_img(request, id):
    try:
        img = Image.obj_img.get(id=id)
        img.delete()
        return redirect('form_up_img')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")