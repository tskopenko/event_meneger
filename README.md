

# Event Management API

## What for?
This application allows managing events, registering for them, and interacting via a REST API.

## How to Run the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/tskopenko/event_meneger.git
   cd event_meneger
   ```

2. Install dependencies (recommended inside a virtual environment):

   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Open in your browser:

   ```
   http://127.0.0.1:8000/api/docs/
   ```

   to access the API documentation.

---

## API Endpoints

* User Registration:
  `POST /api/register/`

* Obtain JWT Token (Login):
  `POST /api/token/`

* Refresh JWT Token:
  `POST /api/token/refresh/`

* List Events:
  `GET /api/events/`

* Event Details:
  `GET /api/events/{id}/`

* Create Event (authentication required):
  `POST /api/events/`

* Update Event:
  `PUT /api/events/{id}/`

* Delete Event:
  `DELETE /api/events/{id}/`

* List Event Registrations (authentication required):
  `GET /api/registrations/`

* Register for an Event:
  `POST /api/registrations/`

---

## Technologies Used

* Python 3.11
* Django
* Django REST Framework
* Simple JWT (authentication)
* drf-spectacular (API documentation)
* Docker (containerization)
* location-field (geolocation support)

---

## Author

Project developed by **Tymofii Skopenko**

---

## Intended Audience

This application is created for **AIDA Recruitment** as part of a technical test assignment.

---

## Additional Information

As per the test assignment requirements, a PDF file with instructions is included (see `/docs/Python_Test.pdf`).
