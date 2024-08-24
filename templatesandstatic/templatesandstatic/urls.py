
from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="Home"),
    path('Index',views.Index,name="Index"),
    path('About',views.About,name="About")
]
