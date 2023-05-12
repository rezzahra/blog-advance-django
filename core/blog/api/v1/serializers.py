from rest_framework import serializers
from blog.models import Post, Category


class PostSerializer(serializers.ModelSerializer):
        snippet = serializers.ReadOnlyField(source='get_snippet')
        class Meta:
            model = Post
            fields = ['id','author', 'image', 'title', 'content', 'snippet','created_date', 'status', 'published_date', ]
            read_only_fields = ['content']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
