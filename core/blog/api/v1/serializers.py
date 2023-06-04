from rest_framework import serializers
from blog.models import Post, Category
from accounts.models import Profile, User


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name="get_abs_url")

    # category = serializers.SlugRelatedField(many=False,slug_field='name',queryset=Category.objects.all())
    # category = CategorySerializer()
    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "image",
            "title",
            "content",
            "category",
            "snippet",
            "created_date",
            "relative_url",
            "status",
            "published_date",
            "absolute_url",
        ]
        read_only_fields = ["content", "author"]

    def get_abs_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snippet", None)
            rep.pop("relative_url", None)
            rep.pop("absolute_url", None)
        else:
            rep.pop("content", None)
        rep["category"] = CategorySerializer(
            instance.category, context={"request": request}
        ).data
        return rep

    def create(self, validated_data):
        # user = User.object.get(id=self.context.get('request').user.id)
        # print(user)
        # post=Profile.objects.get(user=user)
        # print(post)
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]
