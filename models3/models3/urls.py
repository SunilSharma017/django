
from django.contrib import admin
from django.urls import path
from . import views
from . import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Welcome,name="Welcome")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
