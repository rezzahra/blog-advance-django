from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from blog.models import Post, Category
from rest_framework import status
from django.shortcuts import get_object_or_404
# cbv api.view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# cbv generic.view
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
# cbv view set
from rest_framework import viewsets
from rest_framework.decorators import action
from .permissions import IsOwnerOrReadOnly
# filte
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# pagination
from .paginations import LargeResultsSetPagination
"""
    '''getting post list  and create post'''
    
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

'''
class PostListApi(APIView):
    """ getting post list  and create post by api view """
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
'''


'''
class PostListGeneric(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """getting post list  and create new post by GenericAPIView & mixins """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    def get(self, request, *args, **kwargs):
        """ retrieving the post data """
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
'''


# class PostList(ListCreateAPIView):
#     """ getting post list  and create new post by ListCreateAPIView """
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
#



'''
     """ getting detail of the post and edit plus removing it by fbv """
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=pk, status=True)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        post = get_object_or_404(Post, pk=pk, status=True)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post = get_object_or_404(Post, pk=pk, status=True)
        post.delete()
        return Response({'detail':'post removed'}, status=status.HTTP_204_NO_CONTENT) 

    # try: for first if
    #     post = Post.objects.get(pk=pk)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)
    # except Post.DoesNotExist:
    #     return Response({'detail':'post does not exist'}, status=status.HTTP_404_NOT_FOUND)
'''


'''
class PostDetailApi(APIView):
    """getting detail of the post and edit plus removing it by APIView"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self, request, pk):
        """ retrieving the post data """
        post = get_object_or_404(Post, pk=pk, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    def put(self, request, pk):
        """ editing the post data"""
        post = get_object_or_404(Post, pk=pk, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, pk):
        """ deleting the post data"""
        post = get_object_or_404(Post, pk=pk, status=True)
        post.delete()
        return Response({'detail':'post does not exist'}, status=status.HTTP_404_NOT_FOUND)
'''


'''
class PostDetailGeneric(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """getting detail of the post and edit plus removing it by GenericAPIView & mixins """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    def get(self, request, *args, **kwargs):
        """ retrieving the post data """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """ updating the post data """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """ deleting the post data """
        return self.destroy(request, *args, **kwargs)
'''


# class PostDetail(RetrieveUpdateDestroyAPIView):
#     """getting detail of the post and edit plus removing it by RetrieveUpdateDestroyAPIView"""
#     permission_classes= [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
#
class PostModelViewSet(viewsets.ModelViewSet):
    """getting list post & detail of the post by viewsets.ModelViewSet """
    permission_classes= [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {'author':['exact', 'in'], 'category':['exact', 'in'],}
    search_fields = ['content', 'title']
    ordering_fields = ['published_date']
    pagination_class = LargeResultsSetPagination

    @action(detail=False, methods=['get'])
    def get_ok(self, request):
        return Response({'detail':'ok'})


class CategoryModelViewSet(viewsets.ModelViewSet):
    """getting category of the post by viewsets.ModelViewSet """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
