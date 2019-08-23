from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.ArticleList.as_view()),
    path('<int:pk>/', views.ArticleDetail.as_view()),
    path('category/', views.CategoryList.as_view()),
    path('users/', views.UserProfileList.as_view()),
    path('users/<int:pk>/', views.UserProfileDetail.as_view()),
    path('rest-auth/', include('rest_auth.urls'))
]