from django.db import models

# Create your models here.
class Employee(models.Model):
    # TABLE ROWS
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)

    # CREATE / INSERT / ADD - POST
    # RETRIEVE / FETCH - GET
    # UPDATE / EDIT - PUT
    # DELETE / REMOVE - DELETE

