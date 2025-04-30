from django.shortcuts import get_object_or_404, render, redirect
from .forms import EmployeeForm
from .models import Employee


from django.shortcuts import render

def homepage(request):
    return render(request, 'registerapp/homepage.html')

# View to list all employees
def employee_list(request):
    employees = Employee.objects.all()  # Fetch all employee records from the database
    context = {'employee_list': employees}
    return render(request, 'registerapp/employee_list.html', context)

# View to insert a new employee or update an existing one
def employee_form(request, id=None):
    if request.method == 'POST':
        # If this is a POST request, create a form instance and populate it with data from the request
        if id:
            employee = get_object_or_404(Employee, id=id)  # Fetch the employee if id is provided
            form = EmployeeForm(request.POST, instance=employee)  # Pre-fill the form with employee data
        else:
            form = EmployeeForm(request.POST)  # For a new employee, no instance is needed
        
        if form.is_valid():  # Check if form is valid
            form.save()  # Save the data to the database
            return redirect('employee_list')  # Redirect to employee list page
        else:
            # If form is invalid, render the form again with error messages
            return render(request, 'registerapp/employee_form.html', {'form': form})
    
    else:
        # For GET requests, create a new form or pre-fill the form for editing an existing employee
        if id:
            employee = get_object_or_404(Employee, id=id)
            form = EmployeeForm(instance=employee)
        else:
            form = EmployeeForm()
        return render(request, 'registerapp/employee_form.html', {'form': form})


# View to delete an employee by ID
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()  # Delete the employee record
    return redirect('/employee/list')  # Redirect to employee list view after deletion
