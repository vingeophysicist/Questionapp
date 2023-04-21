from django.urls import path
from .views import CreateView, LoginView, ProfileDetailView




app_name = 'account'


urlpatterns = [
    path('register/', CreateView.as_view(), name="create_user"), 
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<int:user__id>/', ProfileDetailView.as_view(), name='profile-detail'),
]
