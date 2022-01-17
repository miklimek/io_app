from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.core.validators import MinLengthValidator
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20, validators=[MinLengthValidator(20)])
    genres = models.ManyToManyField(Genre)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.title


class Opinion(models.Model):
    content = models.CharField(max_length=500)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now=True)
    rating = models.FloatField(validators=[MaxValueValidator(10), MinValueValidator(0)], null=True)

    def __str__(self):
        return self.content
