from django.db import models

from django.contrib.auth.models import AbstractUser
from django.forms import DecimalField


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="dish_images/", null=True, blank=True)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="ingredients_images/", null=True, blank=True)
    dishes = models.ManyToManyField(Dish, related_name="ingredients")

    def __str__(self):
        return self.name
