from .serializers import CreateUserSerializer, ProfileSerializer
from .models import User, Profile
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.generics import UpdateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import authenticate, login
from rest_framework import serializers
from .permissions import IsOwnerOrReadOnly






class CreateView(APIView):
    permission_classes = [AllowAny]
    

    def post(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)




class ProfileDetailView(RetrieveUpdateDestroyAPIView):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user__id'
    permission_classes =  [IsOwnerOrReadOnly]

    









