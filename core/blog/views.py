from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'
        context['posts'] = Post.objects.all()
        return context


# founction base view Redirect
'''
from django.shortcuts import redirect
def redirectmaktab(request):
    return redirect('https://maktabkhooneh.org/')
'''


class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.org'


class PostList(LoginRequiredMixin, ListView):
    model = Post
    # queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 2
    login_url = '/admin/login/'
    redirect_field_name = 're_direct_to'


    # def get_queryset(self):
    #     post = Post.objects.filter(status=True)
    #     return post
    #


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    # fields = ['author', 'title', 'content', 'category', 'status', 'published_date']
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostEdite(UpdateView):
    model = Post
    form_class = PostForm

    # success_url = reverse_lazy('blog:post_list')
    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("blog:post_detail", kwargs={"pk": pk})


class PostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
    permission_required = 'blog.delete_post'