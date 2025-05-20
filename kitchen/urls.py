from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "kitchen"

urlpatterns = [
    path("", views.index, name="index"),
    path("dishes/", views.DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", views.DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", views.DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", views.DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", views.DishDeleteView.as_view(), name="dish-delete"),
    path(
        "dishes/<int:pk>/toggle-assign/",
        views.toggle_assign_to_dish,
        name="toggle-dish-assign",
    ),
    # Cook URLs
    path("cooks/", views.CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", views.CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", views.CookCreateView.as_view(), name="cook-create"),
    path(
        "cooks/<int:pk>/update-experience/",
        views.CookExperienceUpdateView.as_view(),
        name="cook-experience-update",
    ),
    path("cooks/<int:pk>/delete/", views.CookDeleteView.as_view(), name="cook-delete"),
    # Dish Type URLs
    path("dish-types/", views.DishTypeListView.as_view(), name="dish-type-list"),
    path(
        "dish-types/<int:pk>/",
        views.DishTypeDetailView.as_view(),
        name="dish-type-detail",
    ),
    path(
        "dish-types/create/",
        views.DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "dish-types/<int:pk>/update/",
        views.DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish-types/<int:pk>/delete/",
        views.DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path("ingredients/", views.IngredientListView.as_view(), name="ingredient-list"),
    path(
        "ingredients/<int:pk>/",
        views.IngredientDetailView.as_view(),
        name="ingredient-detail",
    ),
    path(
        "ingredients/create/",
        views.IngredientCreateView.as_view(),
        name="ingredient-create",
    ),
    path(
        "ingredients/<int:pk>/update/",
        views.IngredientUpdateView.as_view(),
        name="ingredient-update",
    ),
    path(
        "ingredients/<int:pk>/delete/",
        views.IngredientDeleteView.as_view(),
        name="ingredient-delete",
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="kitchen/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.CookCreateView.as_view(), name="cook-create"),
]
