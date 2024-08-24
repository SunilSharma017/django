from django.http import HttpResponse
from django.shortcuts import render 

def Home(request):
    return render(request,"index.html")

def Index(request):
    return render(request,"two.html")

def About(request):
    return render(request,"three.html")