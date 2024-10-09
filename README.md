CV Upload Application

This is a Django-based web application that allows users to create accounts, upload their CVs in Excel format, and view their uploaded CV data. Administrators can view all user accounts and their corresponding CVs.
Features

    User Registration and Login
    Excel CV Upload (File processing and data storage)
    Display uploaded CVs in JSON format
    Admin view for managing users and their CVs

Project Structure

The project follows a basic Django structure:

    cv_app/: Main project folder
        settings.py: Contains project settings, including database configuration and app registration.
        urls.py: Contains URL routing for the project.
    users/: Contains app-specific logic for handling user registration, login, and CV uploads.
        models.py: Defines CustomUser and CV models.
        views.py: Handles user interactions, file uploads, and data processing.
        forms.py: Contains forms for user registration and CV upload.
        templates/users/: Contains HTML templates for user registration, login, and CV upload.
    media/: Stores uploaded files.

Installation

Clone the repository:
https://github.com/mandan21/cv_app.git
cd cv_app

Set up a virtual environment:

python3 -m venv myvenv

source myvenv/bin/activate  # On Windows use: myvenv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Set up the database: Run migrations to create the necessary database tables:

python manage.py makemigrations
python manage.py migrate

Create a superuser (for admin access):

python manage.py createsuperuser

Run the development server:
    python manage.py runserver

    Access the application at http://127.0.0.1:8000.

Usage
User Registration and Login

    Navigate to the /register/ URL to create a new user account.
    After registering, you will be redirected to the CV upload page.

CV Upload

    On the upload page (/upload/), select an Excel file with your CV information.
    The application will process the Excel file, extract the data, and store it in the database.
    After uploading, you can view the parsed CV data by navigating to the /cv/ URL.

Admin Access

    Admin users can log in to the admin panel at /admin/.
    Admins can view all registered users and their uploaded CVs.

Models

    CustomUser: Extends Django’s AbstractUser to support custom user fields if needed.
    CV: A model that stores the uploaded CV file and its contents as JSON.

CV Model Fields:

    user: One-to-one relationship with CustomUser.
    upload: The uploaded file (stored in the media/cvs/ directory).
    data: Stores the parsed Excel content as JSON.
    uploaded_at: Timestamp of when the CV was uploaded.

Error Handling

    If the uploaded file is not a valid Excel file or contains no data, the user is shown an appropriate error message.
