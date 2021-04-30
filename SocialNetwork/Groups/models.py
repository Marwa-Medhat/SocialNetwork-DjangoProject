from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Group(models.Model):
    name=models.CharField(max_length=50)
    owner=models.CharField(max_length=50)
    creation_date = models.DateField( auto_now=True)
    members = models.ManyToManyField(User, related_name="joinedgroups")

    


    