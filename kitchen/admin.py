from django.contrib import admin
from .models import DishType, Dish, Cook, Ingredient


class IngredientInline(admin.TabularInline):
    model = Ingredient.dishes.through
    extra = 1


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "dish_type", "price", "image_preview")
    list_filter = ("dish_type",)
    search_fields = ("name", "description")
    filter_horizontal = ("cooks",)
    inlines = [IngredientInline]

    exclude = ("ingredients",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image_preview")
    search_fields = ("name",)


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "years_of_experience")
    search_fields = ("username", "first_name", "last_name")

