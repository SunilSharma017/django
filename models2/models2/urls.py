
from django.contrib import admin
from django.urls import path
from . import views
from . import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="Home"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
