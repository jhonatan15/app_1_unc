from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Subject

# Create your views here.
def index(request):
    return HttpResponse('Hello world')

def index(request):
    return render(request, 'index.html')
