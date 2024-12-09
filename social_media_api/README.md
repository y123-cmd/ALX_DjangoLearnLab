# Social Media API

This project is a simple Social Media API built with Django and Django REST Framework (DRF) for user authentication, registration, login, and profile management.

## Features

- User registration, login, and profile management.
- Custom user model with additional fields like `bio`, `profile_picture`, and `followers`.
- Token-based authentication using Django REST Framework's `authtoken`.
- Endpoints for user registration, login, and profile management.

## Prerequisites

- Python 3.8 or higher
- Django 3.x or higher
- Django REST Framework
- PostgreSQL (or any preferred database)

## Installation

Follow these steps to set up the project on your local machine.

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/social-media-api.git
cd social-media-api

Step 2: Set up a virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

Step 3: Install dependencies

pip install -r requirements.txt

Step 4: Set up the database

python manage.py makemigrations
python manage.py migrate

Step 6: Start the development server

python manage.py runserver

