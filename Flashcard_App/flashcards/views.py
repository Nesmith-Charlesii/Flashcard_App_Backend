from django.shortcuts import render
from .models import Collection, Flashcard
from .serializers import CollectionSerializer, FlashcardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CollectionList(APIView):

    def get(self, request):
        collections = Collection.objects.all()
        if collections:
            serializer = CollectionSerializer(collections, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(print("No collections to retrieve"))

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardList(APIView):

    def get(self, request, collection_id):
        collection = Collection.objects.filter(pk=collection_id)
        print("collection", collection)
        if collection:
            flashcards = Flashcard.objects.filter(collection=collection)
            print(flashcards)
            if flashcards:
                serializer = FlashcardSerializer(flashcards, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(print("No info to retrieve"))

    def post(self, request, collection_id):
        serializer = FlashcardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardDetail(APIView):

    def put(self, request, flashcard_id):
        select_flashcard = Flashcard.objects.get(pk=flashcard_id)
        Response(select_flashcard)
        updated_flashcard = FlashcardSerializer(select_flashcard, data=request.data)
        if updated_flashcard.is_valid():
            updated_flashcard.save()
            return Response(updated_flashcard.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_flashcard.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, flashcard_id):
        select_flashcard = Flashcard.objects.get(pk=flashcard_id)
        select_flashcard.delete()
        return Response(status=status.HTTP_200_OK)