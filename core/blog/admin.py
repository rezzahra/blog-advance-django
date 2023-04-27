from django.contrib import admin
from .models import Category, Post
# Register your models here.


class AdminPost(admin.ModelAdmin):
    list_display = [
        'author', 'title', 'status', 'category', 'created_date',
    ]


admin.site.register(Post, AdminPost)
admin.site.register(Category)
