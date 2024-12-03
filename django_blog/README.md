Django Blog Authentication System
Overview
This system enables user registration, login, logout, and profile management for a personalized and secure experience. It uses Django’s built-in authentication features and custom views.

Setup Instructions
Clone the project and navigate to its directory:
bash
Copy code
git clone <your-repo-url>
cd django_blog
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Add blog to INSTALLED_APPS in settings.py and configure URLs:
python
Copy code
path('', include('blog.urls')),
Apply migrations:
bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a superuser:
bash
Copy code
python manage.py createsuperuser
Features
Register: /register - Create an account.
Login: /login - Access your profile.
Logout: /logout - End your session.
Profile Management: /profile - View or update your details.
Testing
Register and verify account creation.
Login and access the profile page.
Update profile details.
Logout and ensure restricted access for unauthenticated users.
Security Notes
CSRF Protection: Enabled for all forms.
Password Hashing: Uses Django’s PBKDF2.
Input Validation: Ensures secure handling of user input.
Future Enhancements
Email verification for registration.
Password reset functionality.
Profile picture support.
