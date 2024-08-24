from django.http import HttpResponse
from django.shortcuts import render,redirect 


def Home(request):
    dct={
        "names":["mohit","anurag","kuldeep","mukul","vishal","nitesh"],
        "ages":[22,23,21,20,19,18],
        "salaries":[50000,45000,40000,35000,33000,32000],
        "job":"yes"
    }
    return render(request,"index.html",dct)


#  django templates : 
#  python : var : html 

# for loop repeatation of code . 

