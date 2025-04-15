from django.db import models

# Create your models here. The class here is the table in the database and the characters under represent the columns in the table.
class User(models.Model):
    id = models.UUIDField()
    full_name = models.CharField(max_length=100)




