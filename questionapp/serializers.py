from rest_framework import serializers
from Questionapp.models import Question, Answer, Subject, Comment




class SubjectSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    
    
    class Meta:
        model = Subject
        field = "__all__"
        
    
class QuestionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    timestamp = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField()
    user_has_answered = serializers.SerializerMethodField()
    coins_given = serializers.IntegerField()
    
    class Meta:
        model = Question
        exclude = ["updated_on"] 
        
    def get_timestamp(self, instance):
        return instance.timestamp.strftime("%B %d, %Y")
    
    def get_answers_count(self, instance):
        return instance.answers.count()
    
    def get_user_has_answered(self, instance):
        request = self.context.get("request")
        return instance.answers.filter(user=request.user).exists()
    
    def get_coins_given(self, instance):
        pass
        
    
    
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
        field = ["text", "timestamp", "user", "question", "answer"]
        
