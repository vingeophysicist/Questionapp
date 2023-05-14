from rest_framework import serializers
from .models import Post, Category
from account.serializers import UserSerializer








class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Category
        fields = ["name", "slug"]



class PostSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    user = UserSerializer(read_only=True)
    #user = serializers.ReadOnlyField(source = 'user.username')
    published = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Post
        fields = ["id","pk", "title", "user_id", "user", "category", "content", "status", "slug", "published"]
        
    def get_published(self, instance):
        return instance.published.strftime("%B %d, %Y")
    
    
    