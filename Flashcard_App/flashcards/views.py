from django.shortcuts import render
from .models import Collection, Flashcard
from .serializers import CollectionSerializer, FlashcardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class CollectionList(APIView):
    def get(self, request):
        collections = Collection.objects.all()
        serializer = CollectionSerializer(collections, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardList(APIView):
    def get(self, request, collection_id):
        collection = Collection.objects.get(pk=collection_id)
        flashcards = Flashcard.objects.filter(collection=collection)
        serializer = FlashcardSerializer(flashcards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, collection_id):
        serializer = FlashcardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)