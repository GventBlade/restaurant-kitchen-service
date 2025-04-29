from django.shortcuts import render, redirect

from kitchen.forms import DishForm
from .models import Dish, DishType, Ingredient


def index(request):
    return render(request, "kitchen/index.html")


def create_dish(request):
    if request.method == "POST":
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("menu")
    else:
        form = DishForm()

    return render(request, "kitchen/create_dish.html", {"form": form})


def menu(request):
    dishes = Dish.objects.select_related("dish_type").prefetch_related("ingredients", "cooks")
    return render(request, "kitchen/menu.html", {"dishes": dishes})