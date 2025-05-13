from django.db import models
from django.contrib.auth.models import User

class JobApplication(models.model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    status = models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')])
    applied_date = models.DateField()
    notes = models.TextField(blank=True)