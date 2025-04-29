from django.contrib import admin
from django.utils.html import mark_safe
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

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" />')
        return "No image"

    image_preview.short_description = 'Image Preview'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image_preview")
    search_fields = ("name",)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" />')
        return "No image"

    image_preview.short_description = 'Image Preview'


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "years_of_experience")
    search_fields = ("username", "first_name", "last_name")

