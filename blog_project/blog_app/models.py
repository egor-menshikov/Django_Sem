from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f'{self.name} {self.surname} {self.email} {self.bio} {self.birthday}'

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    release_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.BigIntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return (f'{self.title} on {self.category} by {self.author.full_name}'
                f' released at {self.release_date.date()}\n{self.content}')


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    commentary = models.TextField()
    submit_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        text = (f'Author: {self.author.full_name}\n'
                f'Article: {self.article.title}\n'
                f'<<<{self.commentary}>>>\n'
                f'Submitted on {self.submit_timestamp}\n')
        if self.update_timestamp:
            text += f'Modified on {self.update_timestamp}'
        return text
