from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import (
IsAuthenticatedOrReadOnly,
BasePermission,
SAFE_METHODS,
DjangoModelPermissionsOrAnonReadOnly
)
from rest_framework.pagination import CursorPagination
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer, UserSerializer



class IsOwnerOrReadOnly(DjangoModelPermissionsOrAnonReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author==request.user

class CustomArticleCursorPagination(CursorPagination):
    page_size=20
    ordering='created'

class ArticleViewSet(ModelViewSet):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes=[IsOwnerOrReadOnly]
    pagination_class=CustomArticleCursorPagination
    authentication_classes=[JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        file = self.request.FILES.get('file')
        if file:
                serializer.save(uploaded_file=File.objects.create(file_name=file.name, file_content=file.read(), mime_type=file.content_type))
        else:
            serializer.save()

class RegisterViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

