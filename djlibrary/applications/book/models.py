from django.db import models

class Autor(models.Model):
    name = models.CharField('Name', max_length=20)
    surname = models.CharField('Surname', max_length=20)
    nationality = models.CharField('Nationality', max_length=15)
    
class Publisher(models.Model):
    name = models.CharField('Name', max_length=30)
    
class Book(models.Model):
    title = models.CharField('Name', max_length=30)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    date = models.DateField('release date')


