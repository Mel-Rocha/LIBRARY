from django.db import models
from enum import Enum

class Language(Enum): 
    ENGLISH = 'English'
    SPANISH = 'Spanish'
    PORTUGUESE = 'Portuguese'


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, blank=True)
    publication_date = models.DateField()
    language = models.CharField(max_length=50, choices=[(language.value, language.name) for language in Language])

    def __str__(self):
        return self.title
    


   
