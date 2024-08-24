from django.shortcuts import render ,redirect 


def Home(request):
    if request.method=="POST":
        return redirect("Result")
    return render(request,"index.html")     
        # return render(request,"success.html",dct)
        
def Result(request):
    dct={}
    if request.method=="POST":
        num1=int(request.POST.get("num1"))
        num2=int(request.POST.get("num2"))
        result=num1+num2
        dct["result"]=result
        dct["num1"]=num1
        dct["num2"]=num2
    return render(request,"success.html")