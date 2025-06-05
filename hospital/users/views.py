from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAdminUser

# Create your views here.
from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAdminUser

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes= [IsAdminUser]  
    
    def create(self, request, *args, **kwargs):
        try:
            serializer= self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response({
                "user": serializer.data,
                "message": "User created successfully"
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password= request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user= authenticate(request, username=username, password=password)

        if user is not None:
            refresh =RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    