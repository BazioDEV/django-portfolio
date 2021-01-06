from django.db import models

#create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    # create next and previous button
    


