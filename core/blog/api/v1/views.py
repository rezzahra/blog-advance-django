from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
# cbv api.view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# cbv generic.v
"""
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
                                          """


class PostList(APIView):
    """getting post list  and create post"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self, request):
        """ retrieving the post data """
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    def post(self,request):
        """ creating the post data """
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

"""
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, id):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({'detail':'post removed'}, status=status.HTTP_204_NO_CONTENT) 

    # try: for first if
    #     post = Post.objects.get(pk=id)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)
    # except Post.DoesNotExist:
    #     return Response({'detail':'post does not exist'}, status=status.HTTP_404_NOT_FOUND)
                                                                                               """


class PostDetail(APIView):
    """getting detail of the post and edit plus removing it"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self, request, id):
        """ retrieving the post data """
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    def put(self, request, id):
        """ editing the post data"""
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        """ deleting the post data"""
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({'detail':'post does not exist'}, status=status.HTTP_404_NOT_FOUND)