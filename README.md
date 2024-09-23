# Django Course and Video API Project

This Django project demonstrates how to display a list of courses with filtering options and a detailed view of videos available for a selected course using simulated API responses in JSON format.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing the API with Postman](#testing-the-api-with-postman)
- [License](#license)

## Features
- List of courses with filtering options (language, subject, etc.).
- Detailed view of videos for a selected course.
- JSON-based API simulation for course and video details.
- Interactive video playback from YouTube links.

## Technologies Used
- **Django**: The web framework used to build the application.
- **Python**: The programming language used.
- **Django Rest Framework**: For creating API endpoints (if added).
- **Bootstrap**: For basic styling (optional).
- **Postman**: For testing API endpoints (optional).

## Installation

### Prerequisites
- Python 3.x
- Django
- Django Rest Framework (if using REST APIs)
- Postman (for testing APIs)

### Step 1: Clone the repository
bash
git clone https://github.com/yourusername/django-course-api.git
cd django-course-api

### Step 2: Create and activate a virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
### Step 3: Install required packages
bash
Copy code
pip install -r requirements.txt
### Step 4: Migrate the database (if applicable)
bash
Copy code
python manage.py migrate
### Step 5: Run the Django server
bash
Copy code
python manage.py runserver
### Project Structure
bash
Copy code
├── your_project/
│   ├── your_app/
│   │   ├── migrations/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── views.py
│   │   ├── models.py
│   │   ├── urls.py
│   └── manage.py
├── get_all_courses_API_response.json
├── get_course_detail_API_response.json
├── README.md
### views.py: 
Contains the views to handle the course list and course detail logic.
### urls.py: 
Defines the URL routes for the application.
### templates/: 
HTML templates for rendering the course list and detail pages.

## Usage
### Course List
The course list page displays all available courses fetched from the simulated API response (get_all_courses_API_response.json).

### Course Detail
When a course is selected from the list, the course detail page shows a list of videos for that course, fetched from the get_course_detail_API_response.json file. Users can play a video directly by clicking on the provided YouTube link.

### urls:
- For the course list:
GET http://127.0.0.1:8000/
- For course details:
GET http://127.0.0.1:8000/<int:course_id>/
### View the response: 
The JSON response with course data will be displayed in the Postman response window.
