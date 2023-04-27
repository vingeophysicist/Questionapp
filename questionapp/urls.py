from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSets



app_name = 'questionapp'


router = DefaultRouter()
router.register(r'question', QuestionViewSets)

urlpatterns = [
   path("", include(router.urls))
]

