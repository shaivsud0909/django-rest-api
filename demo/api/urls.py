from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet,WorkerViewSet
from rest_framework import routers



routers=routers.DefaultRouter()     #Creates a default router that automatically maps your viewsets to URLs.
routers.register(r'company', CompanyViewSet)    #Registers the CompanyViewSet with the router, mapping it to the URL prefix 'company'.
routers.register(r'worker', WorkerViewSet)
urlpatterns = [
     path('',include(routers.urls)),
]
#router examines the URL and HTTP method (GET, POST, etc.) of each request and directs it to the appropriate code that can handle it