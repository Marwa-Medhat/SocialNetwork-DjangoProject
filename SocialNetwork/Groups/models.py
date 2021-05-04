from django.db import models
from Users.models import CustomUser
# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    creation_date = models.DateField(auto_now=True)
    members = models.ManyToManyField(CustomUser, related_name="joinedgroups")
