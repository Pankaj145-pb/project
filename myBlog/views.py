from django.shortcuts import render
from .models import Post, Category, Comment
from .forms import PostForm
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
# # Create your views here.


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')


def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats)
    return render(request, 'myBlog/categories.html', {'cats': cats, 'category_post': category_post})

class IndexView(ListView):
    model = Post
    template_name = "myBlog/index.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "myBlog/post_detail.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context



class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myBlog/create_post.html'


class AddCommentView(CreateView):
    model = Comment
    template_name = 'myBlog/add_comment.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'myBlog/update_post.html'
    fields = ('title', 'text')


class CreateCategoryView(CreateView):
    model = Category
    template_name = 'myBlog/add_category.html'
    fields = ('name',)


class DeletePostView(DeleteView):
    model = Post
    template_name = 'myBlog/delete_post.html'
    fields = '__all__'    