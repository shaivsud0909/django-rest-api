from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
from rest_framework import viewsets
from api.models import Company,Worker
from api.serializers import Companyserializer,Workerserializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = Companyserializer


    #custom url  company/company_id/worker/
    @action(detail=True, methods=['get'])  #detail true means pk is must
    def worker(self, request, pk=None): 
        try:
            comp = Company.objects.get(pk=pk) #This retrieves a single Company object from the database whose primary key (id) matches the value of pk
            emp = Worker.objects.filter(Company=comp)  #This fetches all Worker records where the foreign key field Company (referring to the company model) matches the comp
            serializer = Workerserializer(emp, many=True,context={'request': request})   #json 
            return Response(serializer.data)
        except Company.DoesNotExist:
            return Response({"error": "Company not found"}, status=404)



class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = Workerserializer    


#Views handle the business logic. DRF's ModelViewSet provides default implementations for common actions (CRUD operations).