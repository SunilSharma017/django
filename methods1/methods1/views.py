from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    if request.method=="GET":
        name=request.GET.get("n1")
        email=request.GET.get("n2")
        password=request.GET.get("n3")
        print("name is : ",name)
        print("email is : ",email)
        print("password is : ",password)
    return render(request,"index.html")

def FormData(request):
    if request.method=="GET":
        name=request.GET.get("name")
        email=request.GET.get("email")
        password=request.GET.get("password")
        mobile_Number=request.GET.get("mobile")
        gender=request.GET.getlist("rad")
        subjects=request.GET.getlist("check1")
        print("name is : ",name)
        print("email is : ",email)
        print("password is : ",password)
        print("mobile number is :",mobile_Number)
        lst=[]
        ls=[]
        for i in gender:
            lst.append(i)
        for j in subjects:
            ls.append(j)
        print("gender is : ",lst)
        print("subject is  : ",ls)
    return render(request,"form.html")