from django.shortcuts import render
from rest_framework import generics, status
from .models import Post, Category
from .serializers import PostSerializer
from .permissions import IsAdminUserOrReadOnly
from django.contrib.auth.models import User
from rest_framework.response import Response



class PostList(generics.ListCreateAPIView):
    queryset = Post.PostObjects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminUserOrReadOnly]
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user.id)  # Assign user_id with authenticated user's ID
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CategoryPostList(generics.ListAPIView):
    serializer_class = PostSerializer
    
    
    def get_queryset(self):
        slug = self.kwargs['slug']  # assuming you're passing the category slug in the URL
        category = Category.objects.get(slug=slug)
        return Post.objects.filter(category=category)




class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminUserOrReadOnly]
