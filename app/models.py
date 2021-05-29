from django.db import models


class Bookshelf(models.Model):
    name = models.CharField(max_length = 200,unique = True)
    shelf = models.CharField(max_length = 200)

    def __str__(self):
      return self.name


class Book(models.Model):
    title = models.CharField(max_length = 200)
    
