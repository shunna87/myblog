
from django.urls import path
from . import views
from .views import Post
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', HomeView.as_view(), name = "home"),
   path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
   path('add_post/', AddPostView.as_view(), name ='add_post'),
   path('article/edit/<int:pk>', UpdatePostView.as_view(), name ='update_post'),
   path('article/<int:pk>/delete', DeletePostView.as_view(), name ='delete_post'),
   path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]
