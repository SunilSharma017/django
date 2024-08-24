from django.http import HttpResponse
from django.shortcuts import render,redirect 
from TCAAPP.models import TCASTUDENT 

def Home(request):
    if request.method=="POST":
        name=request.POST.get("n1")
        email=request.POST.get("n2")
        password=request.POST.get("n3")
        TCASTUDENT.objects.create(name=name,email=email,password=password)
    return render(request,'index.html')