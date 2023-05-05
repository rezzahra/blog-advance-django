from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ['id','author', 'image', 'title', 'content', 'created_date', 'status', 'published_date', ]

