from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse


def home(request):
    return HttpResponse("""<h1>Welcome to the Home Page!<h1>""")

def about(request):
    friends = ['Alice', 'Bob', 'Charlie']
    return JsonResponse(friends, safe=False)