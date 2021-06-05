from django.urls import path
from . import views


urlpatterns = [
    path('collections/', views.CollectionList.as_view()),
    path('collection_<int:collection_id>/flashcards/', views.FlashcardList.as_view()),
]
