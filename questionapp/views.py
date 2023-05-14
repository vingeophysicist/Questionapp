from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.generics import ListAPIView
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
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView




class SubjectListAPIView(ListAPIView):
    serializer_class = QuestionSerializer
    
    def get_queryset(self):
        slug = self.kwargs['slug'] 
        subject = Subject.objects.get(slug=slug)
        return Question.objects.filter(subject=subject)
    
    

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
    



class AnswerRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly] 
    



class AnswerClapView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = request.user
        
        answer.clappers.remove(user)
        answer.save()
        
        serializer_context = {"request":request}
        serializer = self.serializer_class(answer, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = request.user
        
        answer.clappers.add(user)
        answer.save()
        
        serializer_context = {"request" : request}
        serializer = self.serializer_class(answer, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)
     



class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all().order_by("-timestamp")
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        kwarg_slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=kwarg_slug)
        serializer.save(user=user, question=question)
        
            
    