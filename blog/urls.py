from re import template
from django import views
from django.urls import path
# from . import views 
from .views import HomeView, ArticleDetailView, AddPostView

urlpatterns = [
    # path("", views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    #we can reference to the primary key to get the specific article
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),

]