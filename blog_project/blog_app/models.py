from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    full_name = str(name) + ' ' + str(surname)
