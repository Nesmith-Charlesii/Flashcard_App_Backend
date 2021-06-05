from django.urls import path
from . import views


urlpatterns = [
    path('collections/', views.CollectionList.as_view()),
    path('<int:collection_id>/flashcards/', views.FlashcardList.as_view()),
]
