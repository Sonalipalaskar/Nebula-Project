# Users/views.py
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer, EmailOTPSerializer, LoginSerializer, ForgotPasswordSerializer, ResetPasswordSerializer

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def verify_user(request):
    serializer = EmailOTPSerializer(data=request.data)
    if serializer.is_valid():
        # Perform verification logic here (send OTP, validate OTP, etc.)
        return Response({'message': 'Verification successful.'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        # Perform login logic here (validate credentials, generate tokens, etc.)
        return Response({'access_token': 'your_access_token', 'refresh_token': 'your_refresh_token'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def forgot_password(request):
    serializer = ForgotPasswordSerializer(data=request.data)
    if serializer.is_valid():
        # Perform forgot password logic here (send reset link, OTP, etc.)
        return Response({'message': 'Reset link sent to your email.'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def reset_password(request):
    serializer = ResetPasswordSerializer(data=request.data)
    if serializer.is_valid():
        # Perform password reset logic here (validate OTP, update password, etc.)
        return Response({'message': 'Password reset successful.'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
