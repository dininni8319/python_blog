from django.shortcuts import render 
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm
# def home(request):
#   return render(request, 'home.html')
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView): 
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    #here you pass all the fields
    # fields = "__all__"
    #python list, here you can decide to leave some fields
    # fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['title', 'title_tag', 'body']



