from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import homepage.views

urlpatterns = [
    path('',homepage.views.home,name='home'),
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('other/',include('other.urls')),
    path('university/',include('university.urls')),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)