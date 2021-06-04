from django.db import models


# Create your models here.
class Collection(models.Model):
    title = models.CharField(max_length=50, default='<unknown>')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Flashcard(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=50)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
