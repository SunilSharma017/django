
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="Home"),
]


# database connection with django using app . 

# step1 : create a form inside html file . 
# step2 : use a method and take data from form to python(django)  . 
# step3 : create app using below command : 
#  python manage.py startapp app_name 
# step4 : mentioned app and database inside settings.py   . 
# for database you have these five things . 
# database_name 
# database_user 
# database_host 
# database_password 
# database_port 

# eg :  'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'djangoTCA1',  # database name 
        # 'USER':'root',         # database user 
        # 'HOST':'localhost',    # database host 
        # 'PASSWORD':'sunil123', # database password 
        # 'PORT':3306   
# create model inside app models.py 
# fields : 
# CharField 
# EmailField 
# IntegerField 
# FileField
# ImageField
# 
# In cmd run these two commands : 
# python manage.py makemigrations  , it create model 
# python manage.py migrate  , it add tables inside database 

# python manage.py  runserver port_number 