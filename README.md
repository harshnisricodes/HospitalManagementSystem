# Hospital Management System

## Project Overview

The Hospital Management System is a CRUD-based web application developed to manage patient information efficiently.

The application allows users to add, view, update, delete, and search patient records through a simple web interface.


## Technologies Used
- HTML
- CSS
- JavaScript
- Python
- Django
- Django REST Framework
- SQLite
- Git
- GitHub
- Postman

## Features
- Add new patient
- View all patients
- Update patient details
- Delete patient records
- Search patients by name
- Patient data validation
- REST API support
- SQLite database
- User-friendly web interface

## Patient Details

The system stores the following patient information:

- Patient ID
- Name
- Age
- Gender
- Phone
- Email
- Disease
- Doctor Name

## CRUD Operations

The application supports the following REST API operations:

| Method | Endpoint | Operation |
|--------|----------|-----------|
| POST | `/api/patients/` | Create Patient |
| GET | `/api/patients/` | View Patients |
| GET | `/api/patients/{id}/` | View One Patient |
| PUT | `/api/patients/{id}/` | Update Patient |
| PATCH | `/api/patients/{id}/` | Partially Update Patient |
| DELETE | `/api/patients/{id}/` | Delete Patient |

## Validation

The application includes validation for:

- Required patient fields
- Valid age
- 10-digit phone number
- Numeric phone number
- Valid email format

## Project Structure

```text
HospitalManagementSystem/
│
├── hospital_api/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── patients/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   └── index.html
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
├── .gitignore
└── README.md
