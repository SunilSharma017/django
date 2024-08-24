from django.http import HttpResponse
from django.shortcuts import render,redirect

def Home(request):
    return render(request,"index.html")
def Download(request):
    return render(request,"download.html")
def Contact(request):
    return render(request,"contact.html")
def Login(request):
    if request.method=="POST":
        name=request.POST.get("n1")
        email=request.POST.get("n2")
        password=request.POST.get("n3")
        gender=request.POST.getlist("rad")
        job=request.POST.getlist("check")
        print("name is : ",name)
        print("email is : ",email)
        print("password is : ",password)
        print("gender is : ",gender)
        print("job is : ",job)
        return redirect("Home")
    return render(request,"login.html")
def Sign(request):
    dct={}
    if request.method=="POST":
        p=int(request.POST.get("n1"))
        r=int(request.POST.get("n2"))
        t=int(request.POST.get("n3"))

        si=(p*r*t)/100
        # dct["si"]=si
        # dct["title"]="navbar in django"
        dct={
            "si":si,
            "title":"navbar in django",
            "p":p,
            "r":r,
            "t":t,
        }
        return render(request,"success.html",dct)
    return render(request,"sign.html")
def About(request):
    return render(request,"about.html")





# views : 

# function / methods  . 

# return redirect("function_name")

# html file  . 
# return render(request,"html_file",dct)