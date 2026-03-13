from django.db import models

class Employee(models.Model):
    emp_id = models.IntegerField()
    emp_name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)

    def __str__(self):
        return self.emp_name
