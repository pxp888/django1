from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        return HttpResponse("Hello, POST.")
    else:
        return HttpResponse("Hello, world.")

