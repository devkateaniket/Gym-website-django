# Gym Website (Django)

A Django-based gym website where customers can join through a web form, and their details are stored in the database.

## Features
- Customer signup and login flow
- Protected home page after login
- Customer join form (available after login)
- Data saved to SQLite database
- Admin panel to view and manage customer records
- Responsive frontend using HTML, CSS, and JavaScript

## Customer Fields Stored
- Full name
- Email
- Phone
- Age
- Gender
- Address
- Plan choice
- Join date

## Project Setup (Windows)
1. Create and activate virtual environment:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```powershell
   python manage.py migrate
   ```
4. Run server:
   ```powershell
   python manage.py runserver
   ```
5. Open in browser:
   - http://127.0.0.1:8000/

## Admin Access
1. Create superuser:
   ```powershell
   python manage.py createsuperuser
   ```
2. Open admin panel:
   - http://127.0.0.1:8000/admin/

## App Routes
- `/signup/` Create customer login account
- `/login/` Login page
- `/logout/` Logout route
- `/` Home page (requires login)
- `/join/` Customer registration page
- `/admin/` Django admin panel
