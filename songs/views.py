from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from .serializers import SongSerializer
from rest_framework import generics
from albums.models import Album
from .models import Song


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Song.objects.filter(album=self.kwargs.get("pk"))

    def perform_create(self, serializer):
        album = get_object_or_404(Album, id=self.kwargs.get("pk"))
        serializer.save(album=album)
