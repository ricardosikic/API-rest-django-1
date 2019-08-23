from django.shortcuts import render
from rest_framework import generics
from .serializers import UserProfileSerializer, UserSerializer, ArticleSerializer, CategorySerializer
from .models import User, UserProfile, Article, Category
from rest_framework.permissions import IsAuthenticated

class UserProfileList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ArticleList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class CategoryList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer