
from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome,name="welcome"),
    path('tca',views.TCA),
    path('tca/java',views.TCAJAVA,name="TCAJAVA")
]


# urlpatterns=[path(''),views.function_name,name="function_name"]




