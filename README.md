# Vehicle Service Management System

A web-based application built with Python, Django, HTML, CSS and MySQL to manage the day-to-day operations of a vehicle service center. It provides a centralized platform for managing customer information, vehicle details, service bookings, service costs and service status.

## Modules

- **Accounts:** staff authentication, customer records, customer login, password reset
- **Service:** service bookings, cost management, status tracking, service history

## Features

- Staff login, dashboard, forgot password and password reset
- Customer login using a unique 5-digit Customer ID
- Customer dashboard
- Add, view, search, update and delete customers
- Vehicle information management and vehicle image upload
- Add, view, update and delete service bookings
- Detailed booking view and service cost management
- Service status tracking: Pending, In Service, Completed, Delivered, Cancelled
- Service history for completed and delivered services
- Django admin panel

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django 5.2 | Web framework |
| HTML | Page structure |
| CSS | Styling |
| MySQL | Database |
| Git / GitHub | Version control and hosting |

## Workflow

Staff Login → Dashboard → Customer Management → Vehicle Details → Service Booking → Service Status → Service Completion → Service History

## Installation

1. Clone the repository
```bash
   git clone https://github.com/mohammedshanvc-droid/Vehicle-Service-Management-System.git
   cd Vehicle-Service-Management-System
```
2. Create and activate a virtual environment
```bash
   python -m venv venv
   venv\Scripts\activate
```
3. Install Django and the MySQL client
```bash
   pip install django mysqlclient pillow
```
4. Create a MySQL database and update the `DATABASES` settings in `settings.py`
5. Run migrations
```bash
   python manage.py migrate
```
6. Create an admin user
```bash
   python manage.py createsuperuser
```
7. Start the server
```bash
   python manage.py runserver
```
8. Open `http://127.0.0.1:8000/` in your browser

## Author

Mohammed Shan V C
