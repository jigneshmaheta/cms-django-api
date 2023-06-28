from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Like
from .serializers import PostSerializer, PostCreateSerializer, LikeSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


class UserAccessPermissions(BasePermission):
    """
    User Access permissions
    - If user is authenticated they can perform any requests
    - If user is unauthenticated they can only perform Get requests
    """

    def has_permission(self, request, view):

        if (request.user.is_authenticated or request.method in ("GET",)):
            return True
        return False


class UserAccessSignupPermissions(BasePermission):

    def has_permission(self, request, view):

        if (request.user.is_authenticated or request.method in ("GET", "POST",)):
            return True
        return False


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserAccessSignupPermissions,)

    def perform_create(self, serializer):
        password = make_password(self.request.data["password"])
        serializer.save(password=password)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Add this line to enforce authentication
    # permission_classes = (UserAccessPermissions,)

    def get_serializer_class(self):
        if self.action == 'create':
            return PostCreateSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user

        if Like.objects.filter(post=post, user=user).exists():
            return Response({'detail': 'You have already liked this post.'}, status=400)

        Like.objects.create(post=post, user=user)
        return Response({'detail': 'Post liked successfully.'}, status=201)

    @action(detail=True, methods=['delete'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user

        try:
            like = Like.objects.get(post=post, user=user)
            like.delete()
            return Response({'detail': 'Post unliked successfully.'}, status=200)
        except Like.DoesNotExist:
            return Response({'detail': 'You have not liked this post.'}, status=400)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    # Add this line to enforce authentication
    permission_classes = (UserAccessPermissions,)


class Login(APIView):
    """
    Logs in an existing user.
    """

    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user = User.objects.filter(username=username).first()
        # check if user valid
        user = authenticate(username=username, password=password)
        if user is None:
            raise AuthenticationFailed(
                "Please enter valid username or password!")
        Token.objects.get_or_create(user=user)  # create or get user token

        tokenAuth = Token.objects.get(user=user)  # get user token
        response = Response()
        response.data = {"token": tokenAuth.key}
        return response
