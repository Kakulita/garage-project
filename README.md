# 🏎️ Virtual Garage & Lap Time Tracker

Welcome to the **Virtual Garage** project! This is a comprehensive web application built with the Django framework that allows car enthusiasts to manage their vehicle collections, record track lap times, and view a competitive leaderboard.

## 🌟 Features Overview

This project satisfies all requirements for a full-stack Django application, including core functionalities, advanced integrations, and a focus on code quality.

### 1. Core Functionality (CRUD & Framework Usage)
*   **Create, Read, Update, Delete (CRUD):** Fully functional CRUD operations for `Car` and `LapTime` objects.
*   **Django MVC/MVT Architecture:** Clean separation of concerns using Models, Views, Templates, URLs, and Forms.
*   **Error Handling & Validation:** Built-in Django form validations ensure robust data integrity and user feedback.

### 2. Database Design & Integrity
*   **Relational Models:** Logical use of `ForeignKey` (e.g., `LapTime` to `Car`, `Car` to `User`) and `ManyToMany` relationships (e.g., `Car` to `Tag`).
*   **Optimized Queries:** Utilizing Django ORM effectively with `select_related` and `prefetch_related` where necessary to avoid N+1 query issues.

### 3. Frontend & User Experience (UI/UX)
*   **Modern UI:** A clean, visually appealing interface using **Bootstrap 5** (via `crispy_bootstrap5`).
*   **Responsive Layout:** Fully responsive grid systems that adapt perfectly to mobile, tablet, and desktop screens.
*   **Intuitive Navigation:** Clear layout with dynamic active states, flash messages, and easy-to-use forms.

### 4. Advanced Features
*   **Authentication System:** Secure login, signup, and logout functionality. Views are protected using `@login_required`.
*   **Search & Filter:** Users can dynamically search their garage by brand/model and filter by fuel type.
*   **RESTful API:** Implemented using **Django REST Framework (DRF)**. Provides JSON endpoints (`/api/cars/`, `/api/laps/`, `/api/tracks/`) for potential third-party integrations.
*   **Cloud Media Storage:** Uses **Cloudinary** for scalable and reliable image hosting.

---

## 🛠️ Technical Documentation

### System Architecture
The application is structured into two main Django apps:
1.  `accounts`: Handles user authentication and registration.
2.  `garage`: The core application handling cars, tracks, lap times, and the REST API.

### Database Schema (Models)
*   `User` (Django Auth): The owner of the cars.
*   `Car`: Stores vehicle specifics (`brand`, `model`, `year`, `fuel_type`, `image`). Has a One-to-Many relationship with `User`.
*   `Track`: Stores track information (`name`, `location`, `length_km`).
*   `LapTime`: Records track performance (`minutes`, `seconds`, `milliseconds`, `date`). Has a Many-to-One relationship with both `Car` and `Track`.
*   `Tag`: Allows dynamic categorization of cars via a Many-to-Many relationship.

### Design Choices
*   **Django Jazzmin:** Integrated a modern, dark-themed admin interface (`django-jazzmin`) to greatly improve the administrative UX.
*   **Whitenoise:** Used for serving static files efficiently in production.
*   **Cloudinary:** Replaced local file storage with Cloudinary to ensure user-uploaded car images persist across ephemeral host deployments (like Render).

---

## 🧪 Testing & Debugging

Extensive unit testing is implemented to ensure application reliability.
To run the test suite:
```bash
python manage.py test
```
The test coverage includes:
*   **Model Tests:** Verifying string representations, default values, and total millisecond calculations for lap times.
*   **View Tests:** Ensuring access control (login required), successful form submissions, and HTTP status codes.
*   **Authentication Tests:** Validating the signup and login flow.

---

## 🚀 Deployment & Setup

The project is successfully deployed on **Render.com**. 
Live Demo: [https://garage-project-1.onrender.com/](https://garage-project-1.onrender.com/)

### Local Setup Instructions
1.  Clone the repository:
    ```bash
    git clone https://github.com/Kakulita/garage-project.git
    cd garage-project
    ```
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run database migrations:
    ```bash
    python manage.py migrate
    ```
5.  Start the development server:
    ```bash
    python manage.py runserver
    ```
