from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField

# Create your models here.

class Trips(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    depature_date = models.DateField()
    arrival_date = models.DateField()
    depature_place = CharField(max_length=255)
    note = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    createAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)