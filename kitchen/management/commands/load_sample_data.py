from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from kitchen.models import DishType, Ingredient, Dish
from django.db.utils import IntegrityError
import random

class Command(BaseCommand):
    help = 'Loads sample data into the database for DishTypes, Ingredients, Cooks, and Dishes.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('--- Starting data creation (Extended) ---'))

        Cook = get_user_model()

        # --- 1. Define and Create Dish Types ---
        self.stdout.write('\nDefining and creating Dish Types...')
        dish_types_data = [
            "Fast-food", "Italian food", "Pasta", "Appetizer", "Main Course",
            "Dessert", "Beverage", "Soup", "Salad", "Breakfast", "Vegetarian",
            "Seafood", "Seafood Soup"
        ]
        created_dish_types = {}
        for dt_name in dish_types_data:
            dish_type, created = DishType.objects.get_or_create(name=dt_name)
            created_dish_types[dt_name] = dish_type
            if created:
                self.stdout.write(self.style.SUCCESS(f"  Created DishType: {dish_type.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"  DishType already exists: {dish_type.name}"))


        # --- 2. Define and Create Ingredients ---
        self.stdout.write('\nDefining and creating Ingredients...')
        ingredients_data = [
            "Cheese", "Salami", "Tomato", "Onion", "Garlic", "Potato", "Carrot",
            "Chicken Breast", "Beef Fillet", "Pork Ribs", "Salmon", "Shrimp",
            "Flour", "Eggs", "Milk", "Sugar", "Butter", "Olive Oil", "Salt",
            "Black Pepper", "Lettuce", "Cucumber", "Bell Pepper", "Rice", "Pasta",
            "Bread", "Mushrooms", "Herbs", "Lemon", "Chocolate", "Vanilla",
            "Burger Bun", "Ground Beef", "Pickles", "Ketchup", "Mustard",
            "Pizza Dough", "Pizza Sauce", "Pepperoni", "Mozzarella",
            "Bacon", "Parmesan Cheese", "Egg Yolk",
            "Clams", "Mussels", "White Wine",
            "Cabbage", "Soy Sauce", "Tofu", "Broccoli", "Red Wine", "Cream", "Coffee Beans", "Whipped Cream"
        ]
        created_ingredients = {}
        for ing_name in ingredients_data:
            ingredient, created = Ingredient.objects.get_or_create(name=ing_name)
            created_ingredients[ing_name] = ingredient
            if created:
                self.stdout.write(self.style.SUCCESS(f"  Created Ingredient: {ingredient.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"  Ingredient already exists: {ingredient.name}"))


        # --- 3. Define and Create Cooks ---
        self.stdout.write('\nDefining and creating Cooks...')
        cooks_data = [
            {"username": "administrator", "first_name": "", "last_name": "", "years_of_experience": 2},
            {"username": "Mashka", "first_name": "Maria", "last_name": "Ivanivna", "years_of_experience": 10},
            {"username": "chef_john", "first_name": "John", "last_name": "Doe", "years_of_experience": 10},
            {"username": "chef_mary", "first_name": "Mary", "last_name": "Smith", "years_of_experience": 7},
            {"username": "chef_david", "first_name": "David", "last_name": "Brown", "years_of_experience": 5},
            {"username": "chef_sarah", "first_name": "Sarah", "last_name": "Miller", "years_of_experience": 12},
            {"username": "chef_alex", "first_name": "Alex", "last_name": "Johnson", "years_of_experience": 8},
            {"username": "chef_olivia", "first_name": "Olivia", "last_name": "Green", "years_of_experience": 6},
        ]
        created_cooks = {}
        for cook_info in cooks_data:
            try:
                cook, created = Cook.objects.get_or_create(
                    username=cook_info["username"],
                    defaults={
                        "first_name": cook_info["first_name"],
                        "last_name": cook_info["last_name"],
                        "years_of_experience": cook_info["years_of_experience"],
                        "password": "pbkdf2_sha256$600000$gSdfd4dFfA0$vYq2zLzP8xK1mN3o4qR5sT6u7vW8xY9z0A1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0"
                    }
                )
                if not created:
                    if cook.first_name != cook_info["first_name"]: cook.first_name = cook_info["first_name"]
                    if cook.last_name != cook_info["last_name"]: cook.last_name = cook_info["last_name"]
                    if cook.years_of_experience != cook_info["years_of_experience"]:
                        cook.years_of_experience = cook_info["years_of_experience"]
                    cook.save()
                    self.stdout.write(self.style.WARNING(f"  Updated existing Cook: {cook.username}"))
                else:
                    cook.set_password("password123")
                    cook.save()
                    self.stdout.write(self.style.SUCCESS(f"  Created Cook: {cook.username} ({cook.first_name} {cook.last_name})"))

                created_cooks[cook_info["username"]] = cook
            except IntegrityError as e:
                self.stdout.write(self.style.ERROR(f"  Error creating cook {cook_info['username']}: {e}"))
                created_cooks[cook_info["username"]] = Cook.objects.get(username=cook_info["username"])

        # --- 4. Define 30 NEW Dishes ---
        self.stdout.write('\nDefining 30 NEW Dishes...')
        dishes_to_add = [
            # 1. New Appetizer
            {
                "name": "Bruschetta with Tomatoes", "description": "Classic Italian appetizer with fresh tomatoes, garlic, and basil on toasted bread.",
                "price": 7.50, "dish_type": "Appetizer", "cooks": ["chef_mary", "Mashka"],
                "ingredients": ["Tomato", "Garlic", "Herbs", "Olive Oil", "Bread"]
            },
            # 2. New Main Course
            {
                "name": "Roasted Chicken with Vegetables", "description": "Tender roasted chicken served with a medley of seasonal vegetables.",
                "price": 19.50, "dish_type": "Main Course", "cooks": ["chef_john", "chef_david"],
                "ingredients": ["Chicken Breast", "Potato", "Carrot", "Onion", "Herbs", "Olive Oil", "Salt", "Black Pepper"]
            },
            # 3. New Dessert
            {
                "name": "Apple Crumble with Vanilla Ice Cream", "description": "Warm apple crumble topped with a crunchy oat topping and a scoop of vanilla ice cream.",
                "price": 10.00, "dish_type": "Dessert", "cooks": ["chef_sarah", "chef_alex"],
                "ingredients": ["Sugar", "Flour", "Butter", "Vanilla"]
            },
            # 4. New Beverage
            {
                "name": "Fresh Orange Juice", "description": "Freshly squeezed orange juice, rich in Vitamin C.",
                "price": 5.00, "dish_type": "Beverage", "cooks": ["chef_mary"], "ingredients": []
            },
            # 5. New Breakfast
            {
                "name": "Scrambled Eggs with Bacon", "description": "Fluffy scrambled eggs served with crispy bacon slices.",
                "price": 8.00, "dish_type": "Breakfast", "cooks": ["Mashka", "chef_david"],
                "ingredients": ["Eggs", "Bacon", "Salt", "Black Pepper"]
            },
            # 6. New Fast-food
            {
                "name": "Cheeseburger Deluxe", "description": "Juicy beef patty with cheese, lettuce, tomato, onion, and special sauce.",
                "price": 10.50, "dish_type": "Fast-food", "cooks": ["chef_john", "chef_olivia"],
                "ingredients": ["Burger Bun", "Ground Beef", "Cheese", "Lettuce", "Tomato", "Onion", "Pickles", "Ketchup", "Mustard"]
            },
            # 7. New Italian Food
            {
                "name": "Risotto with Mushrooms", "description": "Creamy Arborio rice cooked with wild mushrooms and Parmesan cheese.",
                "price": 17.00, "dish_type": "Italian food", "cooks": ["chef_david", "chef_sarah"],
                "ingredients": ["Rice", "Mushrooms", "Onion", "Garlic", "Parmesan Cheese", "White Wine", "Butter", "Olive Oil"]
            },
            # 8. New Pasta
            {
                "name": "Pesto Pasta", "description": "Pasta tossed in vibrant green pesto sauce with pine nuts and Parmesan.",
                "price": 14.00, "dish_type": "Pasta", "cooks": ["chef_mary", "chef_alex"],
                "ingredients": ["Pasta", "Herbs", "Olive Oil", "Parmesan Cheese", "Garlic"]
            },
            # 9. New Seafood
            {
                "name": "Grilled Salmon with Asparagus", "description": "Perfectly grilled salmon fillet served with tender asparagus spears.",
                "price": 23.00, "dish_type": "Seafood", "cooks": ["chef_alex", "chef_sarah"],
                "ingredients": ["Salmon", "Lemon", "Olive Oil", "Salt", "Black Pepper"]
            },
            # 10. New Vegetarian
            {
                "name": "Vegetable Curry", "description": "Rich and fragrant curry with a variety of fresh vegetables in a creamy sauce.",
                "price": 16.00, "dish_type": "Vegetarian", "cooks": ["chef_alex", "Mashka"],
                "ingredients": ["Carrot", "Potato", "Bell Pepper", "Onion", "Garlic", "Coconut Milk", "Rice"]
            },
            # 11. New Soup
            {
                "name": "Tomato Basil Soup", "description": "Hearty and comforting soup made with ripe tomatoes and fresh basil.",
                "price": 8.75, "dish_type": "Soup", "cooks": ["chef_mary", "chef_john"],
                "ingredients": ["Tomato", "Onion", "Garlic", "Herbs", "Cream", "Salt", "Black Pepper"]
            },
            # 12. New Salad
            {
                "name": "Greek Salad", "description": "Refreshing salad with cucumber, tomatoes, olives, feta cheese, and red onion.",
                "price": 9.00, "dish_type": "Salad", "cooks": ["Mashka", "chef_mary"],
                "ingredients": ["Cucumber", "Tomato", "Onion", "Cheese", "Olive Oil", "Salt", "Black Pepper"]
            },
            # 13. Breakfast
            {
                "name": "Pancakes with Berries", "description": "Fluffy pancakes served with a mix of fresh berries and maple syrup.",
                "price": 9.50, "dish_type": "Breakfast", "cooks": ["chef_sarah", "chef_olivia"],
                "ingredients": ["Flour", "Eggs", "Milk", "Sugar", "Butter"]
            },
            # 14. Dessert
            {
                "name": "Tiramisu", "description": "Classic Italian dessert with layers of coffee-soaked ladyfingers and mascarpone cream.",
                "price": 11.00, "dish_type": "Dessert", "cooks": ["chef_david", "chef_sarah"],
                "ingredients": ["Eggs", "Sugar", "Chocolate", "Coffee Beans", "Cream"]
            },
            # 15. Beverage
            {
                "name": "Cappuccino", "description": "Espresso with steamed milk and a layer of foam.",
                "price": 4.50, "dish_type": "Beverage", "cooks": ["chef_mary"],
                "ingredients": ["Coffee Beans", "Milk"]
            },
            # 16. Main Course
            {
                "name": "Beef Stroganoff", "description": "Tender strips of beef in a rich, creamy mushroom sauce, served over noodles.",
                "price": 21.00, "dish_type": "Main Course", "cooks": ["chef_john", "chef_alex"],
                "ingredients": ["Beef Fillet", "Mushrooms", "Onion", "Cream", "Pasta", "Salt", "Black Pepper"]
            },
            # 17. Appetizer
            {
                "name": "Shrimp Cocktail", "description": "Chilled shrimp served with a tangy cocktail sauce.",
                "price": 13.00, "dish_type": "Appetizer", "cooks": ["chef_alex", "chef_mary"],
                "ingredients": ["Shrimp", "Lemon"]
            },
            # 18. Pasta
            {
                "name": "Lasagna Bolognese", "description": "Layers of pasta, rich meat sauce, and creamy béchamel, baked to perfection.",
                "price": 18.50, "dish_type": "Pasta", "cooks": ["chef_david", "chef_john"],
                "ingredients": ["Pasta", "Ground Beef", "Tomato", "Onion", "Garlic", "Cheese", "Milk"]
            },
            # 19. Fast-food
            {
                "name": "Chicken Nuggets", "description": "Crispy chicken pieces, perfect for a quick snack.",
                "price": 7.00, "dish_type": "Fast-food", "cooks": ["chef_olivia"],
                "ingredients": ["Chicken Breast", "Flour", "Salt", "Black Pepper"]
            },
            # 20. Vegetarian
            {
                "name": "Tofu Stir-fry", "description": "Wok-fried tofu and fresh vegetables in a savory sauce.",
                "price": 15.00, "dish_type": "Vegetarian", "cooks": ["chef_alex", "Mashka"],
                "ingredients": ["Tofu", "Bell Pepper", "Broccoli", "Onion", "Garlic", "Soy Sauce", "Rice"]
            },
            # 21. Seafood Soup
            {
                "name": "Bouillabaisse", "description": "Traditional French fish stew with various seafood and vegetables.",
                "price": 26.00, "dish_type": "Seafood Soup", "cooks": ["chef_alex", "chef_sarah"],
                "ingredients": ["Salmon", "Shrimp", "Clams", "Mussels", "Tomato", "Onion", "Garlic", "Herbs", "White Wine"]
            },
            # 22. Main Course
            {
                "name": "Lamb Chops with Mint Sauce", "description": "Juicy grilled lamb chops served with a refreshing mint sauce.",
                "price": 28.00, "dish_type": "Main Course", "cooks": ["chef_john", "chef_david"],
                "ingredients": ["Salt", "Black Pepper", "Herbs"]
            },
            # 23. Breakfast
            {
                "name": "Oatmeal with Fruits", "description": "Warm oatmeal topped with fresh fruits and a drizzle of honey.",
                "price": 6.50, "dish_type": "Breakfast", "cooks": ["Mashka"],
                "ingredients": ["Milk"]
            },
            # 24. Dessert
            {
                "name": "Cheesecake", "description": "Creamy cheesecake with a graham cracker crust and berry topping.",
                "price": 10.00, "dish_type": "Dessert", "cooks": ["chef_sarah", "chef_mary"],
                "ingredients": ["Cheese", "Sugar", "Butter"]
            },
            # 25. Beverage
            {
                "name": "Iced Tea", "description": "Chilled black tea with lemon and a hint of sweetness.",
                "price": 3.50, "dish_type": "Beverage", "cooks": ["chef_mary"],
                "ingredients": ["Lemon", "Sugar"]
            },
            # 26. Italian Food
            {
                "name": "Focaccia with Rosemary", "description": "Soft and airy Italian bread seasoned with rosemary and olive oil.",
                "price": 6.00, "dish_type": "Italian food", "cooks": ["chef_david"],
                "ingredients": ["Flour", "Olive Oil", "Herbs", "Salt"]
            },
            # 27. Salad
            {
                "name": "Chicken Cobb Salad", "description": "Hearty salad with grilled chicken, bacon, eggs, avocado, and blue cheese.",
                "price": 14.50, "dish_type": "Salad", "cooks": ["chef_alex", "Mashka"],
                "ingredients": ["Chicken Breast", "Bacon", "Eggs", "Lettuce", "Tomato", "Cheese"]
            },
            # 28. Soup
            {
                "name": "Broccoli Cheddar Soup", "description": "Creamy soup filled with tender broccoli florets and sharp cheddar cheese.",
                "price": 9.00, "dish_type": "Soup", "cooks": ["chef_mary", "chef_john"],
                "ingredients": ["Broccoli", "Cheese", "Milk", "Onion", "Garlic", "Salt", "Black Pepper"]
            },
            # 29. Main Course
            {
                "name": "Duck Confit", "description": "Crispy duck leg slow-cooked in its own fat, served with potatoes.",
                "price": 27.00, "dish_type": "Main Course", "cooks": ["chef_sarah", "chef_john"],
                "ingredients": ["Potato", "Salt", "Black Pepper"]
            },
            # 30. Pasta
            {
                "name": "Aglio e Olio", "description": "Simple and flavorful pasta dish with garlic, olive oil, and chili flakes.",
                "price": 11.00, "dish_type": "Pasta", "cooks": ["chef_david", "chef_alex"],
                "ingredients": ["Pasta", "Garlic", "Olive Oil", "Herbs", "Salt", "Black Pepper"]
            }
        ]

        # --- Process and Add Dishes ---
        self.stdout.write("\nAdding NEW Dishes...")
        for dish_info in dishes_to_add:
            dish_name = dish_info["name"]
            dish_type_name = dish_info["dish_type"]
            cook_usernames = dish_info["cooks"]
            ingredient_names = dish_info["ingredients"]

            if Dish.objects.filter(name=dish_name).exists():
                self.stdout.write(self.style.WARNING(f"  Dish '{dish_name}' already exists. Skipping."))
                continue

            dish_type_obj = created_dish_types.get(dish_type_name)
            if not dish_type_obj:
                self.stdout.write(self.style.ERROR(f"  ERROR: DishType '{dish_type_name}' for dish '{dish_name}' not found. Skipping this dish."))
                continue

            try:
                dish = Dish.objects.create(
                    name=dish_name,
                    description=dish_info.get("description", ""),
                    price=dish_info["price"],
                    dish_type=dish_type_obj
                )
                self.stdout.write(self.style.SUCCESS(f"  Created NEW Dish: {dish.name}"))

                # Assign cooks
                for username in cook_usernames:
                    cook_obj = created_cooks.get(username)
                    if cook_obj:
                        dish.cooks.add(cook_obj)
                    else:
                        self.stdout.write(self.style.WARNING(f"    WARNING: Cook '{username}' not found for dish '{dish_name}'."))

                # Assign ingredients
                for ing_name in ingredient_names:
                    ingredient_obj = created_ingredients.get(ing_name)
                    if ingredient_obj:
                        dish.ingredients.add(ingredient_obj)
                    else:
                        self.stdout.write(self.style.WARNING(f"    WARNING: Ingredient '{ing_name}' not found for dish '{dish_name}'."))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"  ERROR creating dish '{dish_name}': {e}"))

        self.stdout.write(self.style.SUCCESS('\n--- Data creation finished (Extended) ---'))