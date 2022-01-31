from .models import Person, Leads
from rest_framework import viewsets, permissions
from .serializers import Person_Serializer, Leads_Serializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class = Person_Serializer


class LeadsViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class = Leads_Serializer


