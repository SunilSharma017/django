from django.http import HttpResponse
from django.shortcuts import render 

def Home(request):
    if request.method=="GET":
        name=request.GET.get("n1")
        email=request.GET.get("n2")
        password=request.GET.get("n3")
        print("name is :",name)
        print("email is : ",email)
        print("password is : ",password)

    return render(request,"index.html")
def About(request):
    if request.method=="POST":
        name=request.POST.get("n1")
        email=request.POST.get("n2")
        password=request.POST.get("n3")
        gender=request.POST.getlist("rad")
        job=request.POST.getlist("check")
        print("name is :",name)
        print("email is : ",email)
        print("password is : ",password)
        print("gender is : ",gender)
        print("job is : ",job)
    return render(request,"about.html")