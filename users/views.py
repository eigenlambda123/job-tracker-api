from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterUserSerializer


class RegisterUserView(generics.CreateAPIView):
    """
    CreateAPIView handles POST requests for creating new objects
    """
    # parse and validate registerUser
    serializer_class = RegisterUserSerializer
