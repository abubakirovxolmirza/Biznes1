from django.shortcuts import render
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework import permissions
from .token import get_tokens_for_user
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomTokenObtainPairSerializer
# Create your views here.


class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        tokens = get_tokens_for_user(user)
        
        return Response(tokens)


class ListUsersView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class CustomTokenObtainPairView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
# views.py

# views.py

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser, EmailVerification
from .serializers import CustomUserSerializer

class VerifyEmailView(APIView):
    def post(self, request):
        code = request.data.get('code')
        try:
            verification = EmailVerification.objects.get(code=code)
        except EmailVerification.DoesNotExist:
            return Response({'detail': 'Invalid verification code'}, status=status.HTTP_400_BAD_REQUEST)
        
        if verification.is_expired():
            return Response({'detail': 'Verification code has expired'}, status=status.HTTP_400_BAD_REQUEST)
        
        verification.mark_as_verified()
        user = verification.user
        user.is_active = True  # Можно активировать пользователя здесь
        user.save()

        return Response({'detail': 'Email successfully verified'}, status=status.HTTP_200_OK)
