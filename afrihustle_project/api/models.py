from django.db import models
from uuid import uuid4

# Create your models here. The class here is the table in the database and the characters under represent the columns in the table.
class User(models.Model):
    class user_role(models.TextChoices):
        Worker = "Worker"
        Employer = "Employer"
        Admin = "Admin"


    id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    full_name = models.CharField(max_length=250, blank=False)
    email = models.EmailField(unique=True, blank=False)
    password = models.TextField(blank=False)
    phone_number = models.TextField(blank=False, max_length=20)
    role = models.CharField(max_length=8, choices=user_role.choices)
    location = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)








