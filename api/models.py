from django.db import models

class Book(models.Model):
    owner = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
