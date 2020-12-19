from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.TimeField()
    categories = models.ForeignKey(Category)

    def __str__(self):
        return self.author