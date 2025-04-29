from django import forms
from .models import Dish, DishType, Ingredient, Cook


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'price', 'dish_type', 'cooks', 'ingredients', "image"]

    ingredients = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.all(), widget=forms.CheckboxSelectMultiple)
    cooks = forms.ModelMultipleChoiceField(queryset=Cook.objects.all(), widget=forms.CheckboxSelectMultiple)
