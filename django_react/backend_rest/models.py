from django.db import models
from django.db.models import DateTimeField
from django.db.models import CharField
# Create your models here.
class Person(models.Model):
    name = CharField(max_length=100)
    email = CharField(max_length=100, unique=True)
    message = CharField(max_length=500, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Leads(models.Model):
    name = CharField(max_length=100)
    email = CharField(max_length=100, unique=True)
    message = CharField(max_length=500, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name