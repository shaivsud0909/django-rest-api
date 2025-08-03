from rest_framework import serializers
from api.models import Company,Worker

class Companyserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class Workerserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Worker
        fields="__all__"        

#Serializers convert complex data types (like model instances) to Python native datatypes that can be rendered into JSON/XML.        