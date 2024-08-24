
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="Home"),
    path('Download',views.Download,name="Download"),
    path('firstHtml',views.HtmlFile,name="HtmlFile"),
    path('secondHtml',views.HTMLFILES,name="HtmlFILES"),
    path('css',views.TwoCSS,name="TwoCSs")
]


# create  a url inside url.py file 
# from django.shortcuts import render 
# create a function inside views.py file 
# render html files insert  . 
# render(request,"html file") .
# 
# 
# inside settings.py 
# go into the TEMPLATES LIST 
# inside TEMPLATE LIST go into DIRS 
# DIRS:[BASE_DIR,"templates"]
