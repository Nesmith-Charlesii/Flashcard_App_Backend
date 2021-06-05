from django.urls import path
from . import views


urlpatterns = [
    path('api/collections/', views.CollectionList.as_view()),
    path('api/collection/<int:collection_id>/flashcards/', views.FlashcardList.as_view()),
    path('api/flashcard/<int:flashcard_id>/', views.FlashcardDetail.as_view())
]
