from django.urls import path
from .views import RegisterUserView, ListUsersView, CustomUserDetailView, CustomTokenObtainPairView, VerifyEmailView

urlpatterns = [
    path('register', RegisterUserView.as_view()),
    path('users', ListUsersView.as_view()),
    path('users/<int:pk>', CustomUserDetailView.as_view()),
    path('login', CustomTokenObtainPairView.as_view()),
    path('verify-email', VerifyEmailView.as_view(), name='verify-email'),
]
