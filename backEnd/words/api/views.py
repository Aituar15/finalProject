from rest_framework.generics import ListAPIView
from ..models import Word
from .serializers import ShortSerializer, DetailedSerializer
from rest_framework.response import Response
from rest_framework import status


class GetAllWords(ListAPIView):
    serializer_class = ShortSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            array = Word.objects.all()
            return array


class GetByLanguage(ListAPIView):
    serializer_class = ShortSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            language = self.kwargs.get("language")
            queryset = Word.objects.filter(language=language)
            return sorted(queryset)


class GetByTitle(ListAPIView):
    serializer_class = DetailedSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            language = self.kwargs.get("language")
            symbol = self.kwargs.get("symbol")
            array = Word.objects.filter(language=language).filter(title__startswith=symbol)
            return sorted(array)


class GetById(ListAPIView):
    serializer_class = DetailedSerializer

    def get_queryset(self):
        if self.request.method == 'GET':
            language = self.kwargs.get("language")
            pk = self.kwargs.get("pk")
            array = Word.objects.filter(language=language).filter(pk=pk)
            return sorted(array)
