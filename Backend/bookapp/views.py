from django.shortcuts import render
from .models import Book, Opinion, Genre
from django.contrib.auth.models import User
from .serializers import BookSerializer, OpinionSerializer, UserSerializer, GenreSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('id')
    serializer_class = GenreSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, genre_pk=None):
        if genre_pk:
            books = self.queryset.filter(genres=genre_pk)
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        else:
            serializer = BookSerializer(self.queryset, many=True)
            return Response(serializer.data)

    def retrieve(self, request, pk=None, genre_pk=None):
        if genre_pk:
            books = self.queryset.filter(pk=pk, genres=genre_pk)
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        else:
            serializer = BookSerializer(self.queryset, many=True)
            return Response(serializer.data)


class OpinionViewSet(viewsets.ModelViewSet):
    serializer_class = OpinionSerializer
    queryset = Opinion.objects.all()

    def list(self, request, book_pk=None, user_pk=None):
        if book_pk:
            opinions = self.queryset.filter(book=book_pk)
            serializer = OpinionSerializer(opinions, many=True)
            return Response(serializer.data)
        elif user_pk:
            opinions = self.queryset.filter(user=user_pk)
            serializer = OpinionSerializer(opinions, many=True)
            return Response(serializer.data)
        else:
            serializer = OpinionSerializer(self.queryset, many=True)
            return Response(serializer.data)

    def retrieve(self, request, pk=None, book_pk=None, user_pk=None):
        if book_pk:
            opinions = self.queryset.filter(pk=pk, book=book_pk)
            serializer = OpinionSerializer(opinions, many=True)
            return Response(serializer.data)
        elif user_pk:
            opinions = self.queryset.filter(pk=pk, user=user_pk)
            serializer = OpinionSerializer(opinions, many=True)
            return Response(serializer.data)
        else:
            serializer = OpinionSerializer(self.queryset.filter(id=pk), many=True)
            return Response(serializer.data)
