from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, AnswerCreateAPIView,CommentCreateAPIView, AnswerListView, AnswerRetrieveUpdateDeleteAPIView, AnswerClapView, SubjectListAPIView



app_name = 'questionapp'


router = DefaultRouter()
router.register(r'question', QuestionViewSet)

urlpatterns = [
   path("", include(router.urls)),
   path("question/<slug:slug>/answer/", AnswerCreateAPIView.as_view(), name="create-answer"),
   path('question/<slug:slug>/answers/', AnswerListView.as_view(), name='question_answers'),
   path('answers/<int:pk>/', AnswerRetrieveUpdateDeleteAPIView.as_view(), name='answer_details'),
   path('answers/<int:pk>/clap/', AnswerClapView.as_view(), name='answer_details'),
   path('question/<slug:slug>/comment/', CommentCreateAPIView.as_view(), name='comment'),
   path('subjects/<slug:slug>/', SubjectListAPIView.as_view(), name='subject-questions'),

]
