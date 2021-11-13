from .models import Post
from rest_framework import generics
from .serializers import PostSerialzer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


# Create your views here.

class PostList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerialzer


class PostCreateList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerialzer
    queryset = Post.objects.all()



class PostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerialzer


class PostUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerialzer


class PostDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerialzer
