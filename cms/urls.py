from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, PostViewSet, LikeViewSet, Login

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('posts', PostViewSet)
router.register('likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', Login.as_view(), name='login'),
    
]
