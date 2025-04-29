from django.contrib import admin

from .models import DishType, Dish, Cook

admin.site.register(DishType)
admin.site.register(Dish)
admin.site.register(Cook)

