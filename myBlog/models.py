from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=225, default='Uncategorised')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.id)))

    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.id)))