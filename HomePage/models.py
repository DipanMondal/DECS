from django.db import models

# Create your models here.


class Reviewer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    feedback = models.CharField(max_length=600)