from django.http import HttpResponse

def welcome(request):
    return HttpResponse("welcome in my website ")

def TCA(request):
    return HttpResponse("TCA is the best coaching  in Gurugram ")

def TCAJAVA(request):
    return HttpResponse("Seema Ma'ma teaches best java in Gurugram ")