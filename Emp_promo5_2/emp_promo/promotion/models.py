from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.emp_id  # This will show up in the dropdown
