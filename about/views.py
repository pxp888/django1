from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    print(request)
    return HttpResponse("This would be the about page")
