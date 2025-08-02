from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet
from rest_framework import routers


routers=routers.DefaultRouter()
routers.register(r'company', CompanyViewSet)
urlpatterns = [
     path('',include(routers.urls)),
]
#router examines the URL and HTTP method (GET, POST, etc.) of each request and directs it to the appropriate code that can handle it