from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    full_name = str(name) + ' ' + str(surname)

    def __str__(self):
        return f'{self.full_name}'


# class Article(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     release_date = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     category = models.CharField(max_length=100)
#     views = models.BigIntegerField(default=0)
#     is_published = models.BooleanField(default=False)