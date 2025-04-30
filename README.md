
Employee Management System

This is a basic Django project for managing employee records. It allows you to add, update, view, and delete employee information. The project includes a simple user interface to interact with employee data.
Features

    Employee List: Displays a list of all employees.
    Add Employee: A form to add a new employee.
    Edit Employee: A form to update an existing employee's details.
    Delete Employee: Allows you to delete an employee record.

Requirements

    Python 3.x
    Django 3.x or higher

Setup Instructions

Follow the steps below to set up the project locally.
1. Clone the Repository

Clone the project to your local machine:

git clone https://github.com/your-username/employee-management.git

2. Install Dependencies

Navigate to the project directory and install the required dependencies using pip:

cd employee-management
pip install -r requirements.txt

3. Set Up the Database

Make sure you have a database set up. For SQLite (default in Django), you can skip this step.

Run the migrations to set up the database:

python manage.py migrate

4. Create a Superuser (Optional)

If you want to access Django's admin panel, create a superuser:

python manage.py createsuperuser

Follow the prompts to create the admin user.
5. Start the Development Server

Run the following command to start the Django development server:

python manage.py runserver

By default, the application will be accessible at http://127.0.0.1:8000/.
6. Access the Employee Management App

To access the employee management app, navigate to:

http://127.0.0.1:8000/employee/list

You can add, edit, or delete employee records.
7. Access Django Admin (Optional)

If you've created a superuser, you can log in to the Django admin panel by visiting:

http://127.0.0.1:8000/admin


Contributing

If you'd like to contribute to this project, please fork the repository, make your changes, and create a pull request.
License

This project is licensed under the MIT License - see the LICENSE file for details.
