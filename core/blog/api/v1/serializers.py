from rest_framework import serializers
from blog.models import Post, Category


class PostSerializer(serializers.ModelSerializer):
        snippet = serializers.ReadOnlyField(source='get_snippet')
        relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
        absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
        category = serializers.SlugRelatedField(many=False,slug_field='name',queryset=Category.objects.all())
        # category = CategorySerializer()
        class Meta:
            model = Post
            fields = ['id','author', 'image', 'title', 'content', 'category', 'snippet','created_date', 'relative_url', 'status', 'published_date', 'absolute_url' ]
            read_only_fields = ['content']
        def get_abs_url(self, obj):
            request = self.context.get('request')
            return request.build_absolute_uri(obj.pk)




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
