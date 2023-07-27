
# Service Request Application
This is a Django web application that allows customers to submit service requests online and track the status of their requests. The application uses PostgreSQL as the database to store service requests and their tracking information.

## Problem Statement

A gas utility company is experiencing a high volume of customer service requests. The
company's current system is not able to handle the volume of requests, and customers are
experiencing long wait times and poor service.
Develop a Django application to provide consumer services for gas utilities. The application
would allow customers to submit service requests online, track the status of their requests,
and view their account information.
The application would also provide customer support representatives with a tool to manage
requests and provide support to customers.

Here are some specific features that the Django application should include:
Service requests: The application would allow customers to submit service requests online.
This would include the ability to select the type of service request, provide details about the
request, and attach files.
Request tracking: The application would allow customers to track the status of their service
requests. This would include the ability to see the status of the request, the date and time
the request was submitted, and the date and time the request was resolved.

## Installation

1. Clone the repository:
```
    git clone https://github.com/prat8897/Bynry_repo.git
    
    cd service-request
```

2. Create and activate a virtual environment (optional but recommended):
```
    python -m venv venv
```
On Windows: venv\Scripts\activate

On macOS/Linux: source venv/bin/activate

3. Install the required dependencies:
```
    pip install -r requirements.txt
```

4. Set up PostgreSQL:

- Install PostgreSQL on your system if you haven't already.

- Create a new database for the project in PostgreSQL.

5. Configure the database settings:

Open `service_request/settings.py` and update the following database settings:

```python

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'your_database_name',
		'USER': 'your_database_user',
		'PASSWORD': 'your_database_password',
		'HOST': 'localhost',
		'PORT': '5432',
	}
}
```

6. Apply migrations:
```
python manage.py makemigrations

python manage.py migrate
```

7. Create a superuser account to access the Django admin interface:
```
python manage.py createsuperuser
```

8. Run the development server:

```
python manage.py runserver
```

9. Access the application:
Open your web browser and go to http://127.0.0.1:8000/service/login/ to access the home page.

To access the Django admin interface, go to http://127.0.0.1:8000/admin/ and log in with the superuser account you created.

You can view submitted Service Requests in the admin interface, and edit their status from pending to done here.

## Features

Service requests submission: Customers can submit service requests online. They can select the type of service request, provide details, and attach files.

Request tracking: Customers and admins can track the status of service requests. The status, submission date, and resolution date (for resolved requests) are displayed.