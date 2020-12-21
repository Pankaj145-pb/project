from django.shortcuts import render
from .forms import PostForm, CategoryForm, UserForm
from .models import Post, Category
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,ListView,DetailView
# Create your views here.

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        url = super.get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    
class PostListView(ListView):
     model = Post

     template = "index.html"

class DraftListView(ListView):
    model = Comment
    
@login_required
def index(request):
    return render(request,'index.html')

@login_required
def create_post(request):
    context = {}

    form = PostForm(request.Post or None)
    if form.is_valid():
        form.save()

    context[form] = form
    return render(request,'create_post.html',context)

@login_required
def create_category(request):
    context = {}

    form = CategoryForm(request.Post or None)
    if form.is_valid():
        form.save()

    context[form] = form
    return render(request,'create_category.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    user = authenticate(username, password)

    if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'registration/login.html', {})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

        registered = True

        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'registration/register.html',
                          {'user_form':user_form,
                           'registered':registered})