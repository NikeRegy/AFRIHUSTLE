from django.db import models
from uuid import uuid4

# Create your models here. The class here is the table in the database and the characters under represent the columns in the table.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4())
    full_name = models.CharField(max_length=100)
    age = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.id) 




