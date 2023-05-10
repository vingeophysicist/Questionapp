from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, AnswerCreateAPIView,CommentCreateAPIView, AnswerListView



app_name = 'questionapp'


router = DefaultRouter()
router.register(r'question', QuestionViewSet)

urlpatterns = [
   path("", include(router.urls)),
   path("question/<slug:slug>/answer/", AnswerCreateAPIView.as_view(), name="create-answer"),
   path('question/<slug:slug>/answers/', AnswerListView.as_view(), name='question_answers'),
   path('question/<slug:slug>/comment/', CommentCreateAPIView.as_view(), name='comment'),
   
]
