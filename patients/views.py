from rest_framework import viewsets
from django.shortcuts import render
from .models import Patient
from .serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

def home(request):
    return render(request, 'index.html')    