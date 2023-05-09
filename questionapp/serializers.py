from rest_framework import serializers
from questionapp.models import Question, Answer, Subject, Comment
from account.models import User
from account.serializers import UserSerializer





class SubjectSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    
    
    class Meta:
        model = Subject
        field = "__all__"
        
    
class QuestionSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    user = UserSerializer(read_only=True)
    timestamp = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField(read_only=True)
    user_has_answered = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'label', 'image', 'user_id', 'user', 'timestamp', 'coins_given', 'slug', 'answers_count', 'user_has_answered']
        
    def get_timestamp(self, instance):
        return instance.timestamp.strftime("%B %d, %Y")
    
    def get_answers_count(self, instance):
        return instance.answers.count()
    
    def get_user_has_answered(self, instance):
        request = self.context.get("request")
        return instance.answers.filter(user=request.user.id).exists()
    
   
        
    
    
class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    timestamp = serializers.SerializerMethodField()
    clappers_count = serializers.SerializerMethodField()
    user_has_clapped = serializers.SerializerMethodField()
    question_slug = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Answer
        exclude = ["question", "updated_on", "clappers"]
    
    def get_timestamp(self, instance):
        return instance.timestamp.strftime("%B %d, %Y")
    
    def get_clappers_count(self, instance):
        return instance.clappers.count()
    
    def get_user_has_clapped(self, instance):
        request = self.context.get("request")
        return instance.clappers.filter(pk=request.user.pk).exists()
    
    def get_question_slug(self, instance):
        return instance.question.slug
    
    
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ["text", "timestamp", "user", "question", "answer"]
        
