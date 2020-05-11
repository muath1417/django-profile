from django.db import models

class Project(models.Model):
    title= models.CharField(max_length=100)
    desc = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

class Book(models.Model):
    title= models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/',null=True,blank=True)



def __str__(self):
    return self.title