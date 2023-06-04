from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse

# Create your models here.
# User = get_user_model()


class Post(models.Model):
    """
    this is a class to define posts to blog app
    """

    author = models.ForeignKey(
        "accounts.Profile", on_delete=models.CASCADE, related_name="author"
    )
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"name : {self.author}"

    def get_snippet(self):
        return self.content[0:4]

    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
