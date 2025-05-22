from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from decimal import Decimal

from kitchen.models import DishType, Ingredient, Dish, Cook


class CookModelTest(TestCase):
    """Тести для моделі Cook."""

    def setUp(self):
        """Створення тестового кухаря для використання в тестах."""
        self.cook = get_user_model().objects.create_user(
            username="test_cook",
            password="testpassword123",
            first_name="Test",
            last_name="Cook",
            years_of_experience=5
        )

    def test_cook_creation(self):
        """Перевірка коректного створення кухаря."""
        self.assertEqual(self.cook.username, "test_cook")
        self.assertEqual(self.cook.first_name, "Test")
        self.assertEqual(self.cook.last_name, "Cook")
        self.assertEqual(self.cook.years_of_experience, 5)
        self.assertTrue(self.cook.check_password("testpassword123"))
        self.assertFalse(self.cook.is_staff) # Перевіряємо, що за замовчуванням не є staff
        self.assertFalse(self.cook.is_superuser) # Перевіряємо, що за замовчуванням не є суперкористувачем

    def test_cook_str_method(self):
        """Перевірка методу __str__ моделі Cook."""
        self.assertEqual(str(self.cook), "Test Cook (test_cook)")

        # Перевірка випадку, коли first_name і last_name порожні
        cook_no_name = get_user_model().objects.create_user(
            username="anon_cook",
            password="password"
        )
        self.assertEqual(str(cook_no_name), "anon_cook")

    def test_cook_get_absolute_url(self):
        """Перевірка методу get_absolute_url для Cook."""
        # Django потребує, щоб URL-маршрути були налаштовані для коректної роботи reverse()
        # Якщо у вас ще немає URL-маршруту 'kitchen:cook-detail', цей тест може впасти.
        # Зазвичай, для моделей, де немає прямого детального перегляду, get_absolute_url не потрібен.
        # Припускаємо, що у вас є урл kitchen:cook-detail, що веде на CookDetailView
        expected_url = reverse("kitchen:cook-detail", kwargs={"pk": self.cook.pk})
        self.assertEqual(self.cook.get_absolute_url(), expected_url)


class DishTypeModelTest(TestCase):
    """Тести для моделі DishType."""

    def setUp(self):
        """Створення тестового типу страви."""
        self.dish_type = DishType.objects.create(name="Italian Food")

    def test_dish_type_creation(self):
        """Перевірка коректного створення типу страви."""
        self.assertEqual(self.dish_type.name, "Italian Food")
        self.assertEqual(DishType.objects.count(), 1)

    def test_dish_type_str_method(self):
        """Перевірка методу __str__ моделі DishType."""
        self.assertEqual(str(self.dish_type), "Italian Food")

    def test_dish_type_unique_name(self):
        """Перевірка унікальності назви типу страви."""
        with self.assertRaises(Exception): # Очікуємо виняток IntegrityError
            DishType.objects.create(name="Italian Food")

    def test_dish_type_get_absolute_url(self):
        """Перевірка методу get_absolute_url для DishType."""
        expected_url = reverse("kitchen:dish-type-detail", kwargs={"pk": self.dish_type.pk})
        self.assertEqual(self.dish_type.get_absolute_url(), expected_url)


class IngredientModelTest(TestCase):
    """Тести для моделі Ingredient."""

    def setUp(self):
        """Створення тестового інгредієнта."""
        self.ingredient = Ingredient.objects.create(name="Tomato")

    def test_ingredient_creation(self):
        """Перевірка коректного створення інгредієнта."""
        self.assertEqual(self.ingredient.name, "Tomato")
        self.assertEqual(Ingredient.objects.count(), 1)

    def test_ingredient_str_method(self):
        """Перевірка методу __str__ моделі Ingredient."""
        self.assertEqual(str(self.ingredient), "Tomato")

    def test_ingredient_unique_name(self):
        """Перевірка унікальності назви інгредієнта."""
        with self.assertRaises(Exception): # Очікуємо виняток IntegrityError
            Ingredient.objects.create(name="Tomato")

    def test_ingredient_get_absolute_url(self):
        """Перевірка методу get_absolute_url для Ingredient."""
        expected_url = reverse("kitchen:ingredient-detail", kwargs={"pk": self.ingredient.pk})
        self.assertEqual(self.ingredient.get_absolute_url(), expected_url)


class DishModelTest(TestCase):
    """Тести для моделі Dish."""

    def setUp(self):
        """Створення тестових даних для Dish."""
        self.dish_type = DishType.objects.create(name="Main Course")
        self.cook1 = get_user_model().objects.create_user(username="cook1", password="p1", years_of_experience=5)
        self.cook2 = get_user_model().objects.create_user(username="cook2", password="p2", years_of_experience=3)
        self.ingredient1 = Ingredient.objects.create(name="Chicken")
        self.ingredient2 = Ingredient.objects.create(name="Rice")

        self.dish = Dish.objects.create(
            name="Chicken Curry",
            description="Spicy chicken curry with rice.",
            price=Decimal("15.99"),
            dish_type=self.dish_type
        )
        self.dish.cooks.add(self.cook1, self.cook2)
        self.dish.ingredients.add(self.ingredient1, self.ingredient2)

    def test_dish_creation(self):
        """Перевірка коректного створення страви."""
        self.assertEqual(self.dish.name, "Chicken Curry")
        self.assertEqual(self.dish.description, "Spicy chicken curry with rice.")
        self.assertEqual(self.dish.price, Decimal("15.99"))
        self.assertEqual(self.dish.dish_type, self.dish_type)
        self.assertEqual(self.dish.cooks.count(), 2)
        self.assertIn(self.cook1, self.dish.cooks.all())
        self.assertIn(self.cook2, self.dish.cooks.all())
        self.assertEqual(self.dish.ingredients.count(), 2)
        self.assertIn(self.ingredient1, self.dish.ingredients.all())
        self.assertIn(self.ingredient2, self.dish.ingredients.all())
        self.assertEqual(Dish.objects.count(), 1)

    def test_dish_str_method(self):
        """Перевірка методу __str__ моделі Dish."""
        self.assertEqual(str(self.dish), "Chicken Curry")

    def test_dish_relations(self):
        """Перевірка зв'язків між моделями."""
        # Перевірка, що тип страви знає свої страви
        self.assertIn(self.dish, self.dish_type.dishes.all())

        # Перевірка, що кухар знає страви, які він готує
        self.assertIn(self.dish, self.cook1.dishes.all())
        self.assertIn(self.dish, self.cook2.dishes.all())

        # Перевірка, що інгредієнт знає страви, в яких він використовується
        self.assertIn(self.dish, self.ingredient1.dishes.all())
        self.assertIn(self.dish, self.ingredient2.dishes.all())

    def test_dish_price_decimal_precision(self):
        """Перевірка точності десяткового поля ціни."""
        another_dish = Dish.objects.create(
            name="Salad",
            price=Decimal("9.95"),
            dish_type=self.dish_type
        )
        self.assertEqual(another_dish.price, Decimal("9.95"))
        self.assertEqual(another_dish.price.as_tuple().digits, (9, 9, 5)) # Перевірка кількості цифр

    def test_dish_get_absolute_url(self):
        """Перевірка методу get_absolute_url для Dish."""
        expected_url = reverse("kitchen:dish-detail", kwargs={"pk": self.dish.pk})
        self.assertEqual(self.dish.get_absolute_url(), expected_url)
