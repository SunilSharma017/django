from django.shortcuts import render

from django.core.mail import send_mail,EmailMessage

def Home(request):
    # lst=["mohit","anurag","kuldeep","mukul","vishal","nitesh"]
    dct={"names":["mohit","anurag","kuldeep","mukul","vishal","nitesh"],
         "marks":[80,70,90,90,87,75],
         "course":"django",
         "title":"django tempaltes and file attatch with email ",
         }
    # return render(request,"index.html",{"lst":lst})
    return render(request,"index.html",dct)
def EmailFile(request):
    if request.method=="POST":
        try:
            nam=request.POST.get("n1")
            print(nam)
            email=request.POST.get("n2")
            print(email)
            file=request.FILES.get("n3")
            print(file)
            subject="django files "
            message=f"Hey{nam} you are doing good "
            from_email="sharmasunil7742@gmail.com"
            recipient_list=[email]
            email=EmailMessage(subject,message,from_email,recipient_list)
            # file_path=r"C:\Users\Admin\Downloads\python_4pm_20th_August.pdf"
            email.attach_file(file)
            # email.attach(file_path)
            email.send()
        except Exception as e: 
            print(e)

    
    return render(request,"form.html")

    