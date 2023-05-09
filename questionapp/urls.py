from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, AnswerCreateAPIView,CommentCreateAPIView



app_name = 'questionapp'


router = DefaultRouter()
router.register(r'question', QuestionViewSet)

urlpatterns = [
   
   path("", include(router.urls)),
   path("question/<slug:slug>/answer/", AnswerCreateAPIView.as_view(), name="create-answer"),
   path('question/<slug:question_slug>/comments/', CommentCreateAPIView.as_view(), name='question_comments_create'),
   path('answer/<slug:answer_slug>/comments/', CommentCreateAPIView.as_view(), name='answer_comments_create'),
   
]
