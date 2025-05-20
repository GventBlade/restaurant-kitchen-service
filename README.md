# Restaurant Kitchen Service

This project is a management system for a restaurant kitchen,
designed to improve communication and organization among chefs.
It allows chefs to create new dishes and their types,
and to specify the cooks responsible for preparing each dish.

## Table of Contents

* [Features](#features)
* [Database Structure](#database-structure)
* [Installation](#installation)
* [Usage](#usage)
* [Requirements](#requirements)
* [License](#license)

## Features

* **Cook Management:**
    * Cook registration and authentication.
    * View a list of cooks and their details (experience, dishes they can prepare).
    * Update a cook's years of experience.
    * Assign/unassign a cook to/from a dish.
* **Dish Management:**
    * Create, view, update, and delete dishes.
    * Detailed view of dish information (price, description, type, cooks, ingredients).
    * Assign cooks and ingredients to a dish.
* **Dish Type Management:**
    * Create, view, update, and delete dish types.
    * View dishes belonging to a specific type.
* **Ingredient Management:**
    * Create, view, update, and delete ingredients.
    * View dishes that use a specific ingredient.
* **Search and Pagination:**
    * Ability to search by name/username in lists.
    * Pagination for all lists for convenient Browse of large datasets.
* **User-Friendly Interface:** Utilizes Bootstrap and Crispy Forms for a responsive and appealing visual design.

## Database Structure

The project includes the following models:

* **`Cook`** (extends `AbstractUser`):
    * `username` (string)
    * `first_name` (string)
    * `last_name` (string)
    * `years_of_experience` (positive integer)
    * Additional `AbstractUser` fields (email, password, etc.).
    * `groups` (ManyToMany to `auth.Group`)
    * `user_permissions` (ManyToMany to `auth.Permission`)
* **`DishType`**:
    * `name` (string, unique)
* **`Ingredient`**:
    * `name` (string, unique, blank)
* **`Dish`**:
    * `name` (string)
    * `description` (text, optional)
    * `price` (decimal)
    * `dish_type` (ForeignKey to `DishType`)
    * `cooks` (ManyToMany to `Cook` - `settings.AUTH_USER_MODEL`)
    * `ingredients` (ManyToMany to `Ingredient`, optional)

## Installation

To set up and run the project, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/GventBlade/restaurant-kitchen-service.git](https://github.com/GventBlade/restaurant-kitchen-service.git)
    cd restaurant-kitchen-service
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # For Windows
    venv\Scripts\activate
    # For macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a `requirements.txt` file, create one by adding `django`, `django-crispy-forms`, `crispy-bootstrap5`, and any other dependencies you used.)*

4.  **Configure the database:**
    * Ensure your `settings.py` file has the database configured (Django uses SQLite by default).
    * Add `kitchen` to `INSTALLED_APPS` in `settings.py`.
    * Specify your custom user model in `settings.py`: `AUTH_USER_MODEL = 'kitchen.Cook'`.

5.  **Run database migrations:**
    ```bash
    python manage.py makemigrations kitchen
    python manage.py migrate
    ```

6.  **Create a superuser (administrator):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to enter a username, email, and password.

7.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

Open your web browser and navigate to:

* **`http://127.0.0.1:8000/`** - Main service page.
* **`http://127.0.0.1:8000/admin/`** - Django administrative panel.

Log in using superuser or a registered cook's credentials to access the application's functionality.

**Admin Panel Access:**
* **Login:** `administrator`
* **Password:** `admin`

## Requirements

* Python 3.x
* Django 4.x (or higher, depending on your setup)
* django-crispy-forms
* crispy-bootstrap5
* Bootstrap 5 (linked in your base template)
* Bootstrap Icons (linked in your base template)

## License

[Specify your license here, e.g., MIT License or another. If you're unsure, you can simply remove this section or state "All rights reserved by the author."]