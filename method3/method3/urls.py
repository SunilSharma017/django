
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="Home"),
    path('downloads/',views.Download,name="Download"),
    path('about/',views.About,name="About"),
    path('login/',views.Login,name="Login"),
    path('sign-in/',views.Sign,name="Sign"),
    path('contact/',views.Contact,name="Contact"),
]
