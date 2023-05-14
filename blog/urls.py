from django.urls import path, include
from .views import PostList, PostDetails,  CategoryPostList



app_name = "blog"


urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<slug:slug>/', PostDetails.as_view(), name='post-retrieve-update-destroy'),
    path('categories/<slug:slug>/',  CategoryPostList.as_view(), name='post-list-create'),
]