from django.urls import path, re_path
from .import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('my-form', views.my_form, name='my_form'),
    path('my-form2', views.my_form2, name = 'my_form2'),
    path('my-form3', views.my_form3, name="my_form3"),
    # path('about/', TemplateView.as_view(template_name='firstapp/about.html')),
    # path('contact/', TemplateView.as_view(
    #     template_name='firstapp/contact.html',
    #     extra_context={"work": "Разработка программных продуктов"})),
    # re_path(r"^contact/", views.contact),
    # re_path(r"^about/", views.about),
    # re_path(r"^products/(?P<product_id>\d+)/", views.products),
    path("products/<int:product_id>/", views.products),
    path("products/", views.products),  # Маршрут для продукта по умолчанию
    # re_path(r"^products/$", views.products), # Маршрут для продукта по умолчанию
    # re_path(r"^users/(?P<id>\d+)/(?P<name>\D+)/", views.users),
    path("users/", views.users),  # Маршрут для продукта по умолчанию
    path("users/<int:id>/<str:name>/", views.users),
    path("details", views.details),
    path("access/<int:age>", views.access),
]
