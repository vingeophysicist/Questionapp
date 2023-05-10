from django.shortcuts import render
from rest_framework import generics, viewsets
from questionapp.models import Question, Answer, Subject, Comment
from questionapp.serializers import QuestionSerializer, AnswerSerializer, SubjectSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from questionapp.permissions import IsAuthorOrReadOnly
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from account.models import User, Profile
from account.serializers import CreateUserSerializer, ProfileSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from account.models import Profile





class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.get(id=1)
    serializer_class = SubjectSerializer
    
    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-timestamp")
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    lookup_field = "slug"
    
    def perform_create(self, serializer):
        user = self.request.user
        profile_id = self.request.data.get('profile_id')
        coins = self.request.data.get('coins_given')
        profile = Profile.objects.get(user=user)
        
        if profile.coin < int(coins):
            raise serializers.ValidationError("Not enough coins.")
        profile.coin -= int(coins)
        profile.save()
        serializer.save(user=user)
       
    
    @action(detail=False, methods = ['get'])
    def subjects(self, request, subject=None):
        queryset = self.queryset
        if subject:
            queryset = queryset.filter(subject=subject)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
      
        



class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all().order_by("-timestamp")
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        user = self.request.user
        kwarg_slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=kwarg_slug)

        if question.answers.filter(user=user).exists():
            raise ValidationError("You can't answer the question!!!")
        serializer.save(user=user, question=question)
        profile = Profile.objects.get(user=user)
        profile.coin += question.coins_given
        profile.save()
        
class AnswerListView(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Answer.objects.filter(question__slug=slug).order_by("-timestamp")



class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all().order_by("-timestamp")
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        kwarg_slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=kwarg_slug)
        serializer.save(user=user, question=question)
        
            
    