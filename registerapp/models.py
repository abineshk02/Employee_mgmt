from django.db import models
from django.utils import timezone

from django.db import models
from django.utils import timezone

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(default='default@example.com')
    date_joined = models.DateField(default=timezone.now)
    position = models.CharField(max_length=50)  # Now a plain text field inside Employee

    def __str__(self):
        return self.fullname
