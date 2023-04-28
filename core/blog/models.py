from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.
# User = get_user_model()


class Post(models.Model):
    '''
       this is a class to define posts to blog app
    '''

    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'name : {self.author}'


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

