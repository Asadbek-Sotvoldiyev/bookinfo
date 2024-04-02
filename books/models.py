from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    image = models.ImageField(upload_to='books/', blank=True, null=True)
    year = models.IntegerField()
    about = models.TextField()
    piece_of_the_book = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    given_stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.user} rated to {self.book} stars given {self.given_stars}"

class SiteDesign(models.Model):
    image = models.ImageField(upload_to='site/', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()