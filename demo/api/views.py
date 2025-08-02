from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import Company
from api.serializers import Companyserializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = Companyserializer


#Views handle the business logic. DRF's ModelViewSet provides default implementations for common actions (CRUD operations).