from django.db import models

class Employee(models.Model):
    class Meta:
        app_label = 'projectNWC'
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
