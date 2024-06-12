from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100, null=True)
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    earnings = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
