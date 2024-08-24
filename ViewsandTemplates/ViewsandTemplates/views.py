from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return HttpResponse("this is our home page")

def Download(request):
    return HttpResponse("this is download page ")

def HtmlFile(request):
    return render(request,"index.html")

def HTMLFILES(request):
    return render(request,"one.html")

def TwoCSS(request):
    return render(request,"two.html")



#  HttpResponse : for sending text 
#  render : for sending html file .  