# My Site - Practice Project

This is a practice project to learn Python and Django. The goal of this project is to explore Django's features, including models, views, templates, and the admin interface, while building a simple blog application.

## Features

- **Blog Posts**: Create, read, and manage blog posts.
- **Authors**: Associate posts with authors.
- **Tags**: Categorize posts using tags.
- **Admin Interface**: Manage content through Django's built-in admin panel.

## Technologies Used

- **Python**: Programming language.
- **Django**: Web framework for building the application.
- **SQLite**: Default database for development.

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd my_site
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Open the application in your browser at http://127.0.0.1:8000.

## Learning Goals

Understand Django's ORM and how to define models.
Learn how to create views and templates.
Explore Django's admin interface for managing data.
Practice using forms and validators.
Future Improvements
Add user authentication.
Implement a comment system for blog posts.
Enhance the UI with CSS frameworks like Bootstrap or Tailwind.
