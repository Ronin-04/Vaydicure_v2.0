from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    available_days = models.CharField(max_length=50)  # e.g., "Monday - Friday" or specific days
    available_time = models.CharField(max_length=20)  # e.g., "8:00 AM - 2:00 PM"
    url = models.CharField(max_length=300, blank=True, null=True)