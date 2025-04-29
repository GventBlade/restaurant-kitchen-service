from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.menu, name="menu"),
    path("menu/create/", views.create_dish, name="create_dish"),
]
