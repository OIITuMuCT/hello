from django.urls import path, re_path
from .import views


urlpatterns = [
    re_path(r"^contact/", views.contact),
    re_path(r"^about/", views.about),
    # re_path(r"^products/(?P<product_id>\d+)/", views.products),
    path("products/<int:product_id>/", views.products),
    path("products/", views.products),  # Маршрут для продукта по умолчанию
    # re_path(r"^products/$", views.products), # Маршрут для продукта по умолчанию
    # re_path(r"^users/(?P<id>\d+)/(?P<name>\D+)/", views.users),
    path("users/", views.users),  # Маршрут для продукта по умолчанию
    path("users/<int:id>/<str:name>/", views.users),
    path("", views.index),
]
