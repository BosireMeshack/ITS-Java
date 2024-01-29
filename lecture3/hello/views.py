from django.shortcuts import render

from django.http import HttpResponse 
# Create your views here.

def index(request):
    return render(request, "hello/index.html")
def greet(request, city):
    return render(request,"hello/greet.html", {
        "city" : city.capitalize()
    })