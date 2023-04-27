from django.shortcuts import render
from rest_framework import generics, viewsets
from questionapp.models import Question, Answer, Subject
from questionapp.serializers import QuestionSerializer, AnswerSerializer, SubjectSerializer
from rest_framework.permissions import IsAuthenticated
from questionapp.permissions import IsAuthorOrReadOnly
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError



class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    

class QuestionViewSets(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-timestamp")
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    lookup_field = "slug"
    
    def get_queryset(self):
        pass
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        question = get_object_or_404(Question, slug=kwarg_slug)
        if question.answers.filter(user=request_user).exists():
            raise ValidationError("You have already answered this question!!!")
        serializer.save(user=request.user, question=question)





