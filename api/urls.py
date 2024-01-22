from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, RegisterViewSet
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static


router=DefaultRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns=[
    path('register/', RegisterViewSet.as_view({'post':'create'}), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh-token'),
    path('', include(router.urls))
]
