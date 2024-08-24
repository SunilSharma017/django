from django.http import HttpResponse
from django.shortcuts import render,redirect 
from tcapp.models import tcastudent

def Welcome(request):
    if request.method=="POST":
        name=request.POST.get("n1")
        image=request.FILES.get("n2")
        resume=request.FILES.get("n3")
        tcastudent.objects.create(name=name,image=image,resume=resume)
    return render(request,"index.html")
