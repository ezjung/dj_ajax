from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User

from profiles.models import Profiles

# Create your models here.

class Post(models.Model):

    title = CharField(max_length=200)
    body = models.TextField()
    liked = models.ManyToManyField(User, blank=True)
    author = models.ForeignKey(Profiles, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)