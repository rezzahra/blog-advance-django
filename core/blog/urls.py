from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index_2'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('go-to-maktab/', views.RedirectToMaktab.as_view(), name='redirect_maktab'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edite/', views.PostEdite.as_view(), name='post_edite'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('api/v1/', include('blog.api.v1.urls'), name='api_v1')
]
