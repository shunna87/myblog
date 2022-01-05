from django.forms import fields
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class  HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering =['-post_date']


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category = cats)
    return render(request, 'categories.html', {'cats': cats.title(), 'category_posts': category_posts} ) 

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm 
    template_name = 'add_post.html'  
    #fields = '__all__'  
    #fields = ('title', 'body')

class AddCategoryView(CreateView):
    model = Category
   
    template_name = 'add_category.html' 
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm 
    template_name = 'update_post.html'
    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    #fields = ['title', 'body']



