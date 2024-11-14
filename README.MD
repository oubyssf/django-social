# Social Website Project

This project is a social platform built using Django, where users can register, authenticate, share images, and interact with each other. The website allows users to bookmark images from across the web, follow other users, and view activity streams. 

The project is broken into several chapters, with each chapter adding distinct features such as user authentication, social login, image bookmarking, and user interaction functionality.

## Features

- **User Registration and Authentication**
  - Custom user registration views
  - Password management (reset/change)
  - User profile editing
  - Authentication using Django's built-in framework
  - Social authentication via Google using Python Social Auth
  - Profile creation for social auth users

- **Image Bookmarking System**
  - Bookmark and share images from other websites
  - Image thumbnails generation
  - Infinite scroll pagination
  - Many-to-many relationships for bookmarking

- **User Interaction and Activity Stream**
  - Follow/unfollow other users
  - User activity stream for following users' actions
  - Redis integration to track item views and create a ranking of the most viewed images
  - Optimized QuerySets for better performance with related models

- **JavaScript Integration**
  - Asynchronous requests for dynamic page updates
  - JavaScript bookmarklet for image sharing
  - Custom form handling and interactions

## Installation

### Prerequisites

- Python 3.x
- Django 4.x or higher
- Redis (for caching and activity tracking)
- pip (for managing dependencies)

### Steps to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/oubyssf/django-social.git
   cd social-website

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Set up the database:
   ```bash
   python manage.py migrate

5. Create a superuser to access the Django admin panel
   ```bash
   python manage.py createsuperuser

6. Run the development server:
   ```bash
   python manage.py runserver
   python manage.py runserver_plus --cert cert.cert # for running development server on https



