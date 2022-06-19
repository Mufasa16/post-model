from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

    # Author : A Foreign Key to the current user model. Make use of Django’s get_user_model function.
    Author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)