from django.http import HttpResponse
from django.shortcuts import render,redirect
from suntech.models import Person
from django.core.mail import EmailMessage,send_mail
import os
def Home(request):
    if request.method=="POST":
        name=request.POST.get("n1")
        email=request.POST.get("n2")
        password=request.POST.get("n3")
        resume=request.FILES.get("n4")
        print(resume)
        Person.objects.create(name=name,email=email,password=password,resume=resume)
        subject="django files "
        message=f"Hey{name} you are doing good "
        from_email=os.getenv('sharmasunil7742@gmail.com')
        recipient_list=[email]
        mail=EmailMessage(subject,message,from_email,recipient_list)
            # file_path=r"C:\Users\Admin\Downloads\python_4pm_20th_August.pdf"
        mail.attach_file('python_7pm_21th_August.pdf')
            # email.attach(file_path)
        mail.send()
    return render(request,"index.html")