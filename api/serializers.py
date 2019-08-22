from rest_framework import serializers
from .models import User, UserProfile, Article, Category

class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'name', 'dob', 'address', 'city', 'comuna', 'photo')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True,)

    class Meta:
        model = User
        fields = ('id', 'url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}


class ArticleSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Article
        fields = ('id', 'photo', 'title', 'content', 'user', 'category', 'created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')