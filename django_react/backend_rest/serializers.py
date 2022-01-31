from rest_framework import serializers
from .models import Person, Leads

class Person_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'email', 'message', 'created_at']

class Leads_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = ['id', 'name', 'email', 'message', 'created_at']

