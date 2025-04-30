from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),  # Create new employee
    path('<int:id>/', views.employee_form, name='employee_update'),  # Update existing employee
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),  # Delete employee
    path('list/', views.employee_list, name='employee_list'),  # List all employees
]
