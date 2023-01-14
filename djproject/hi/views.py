from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"hi/index.html")

def brian (request):
    return HttpResponse("Hi brian") 

def david (request):
    return HttpResponse("Hi david")
    
def greet(request,name):
    return render(request, "hi/greet.html", {
        "name": name.capitalize()
    })

