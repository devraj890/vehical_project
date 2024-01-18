from django.urls import path, include
from . import views
from .views import signup
from django.conf import settings
from django.conf.urls.static import static
# urls.py

from django.contrib.admin import AdminSite

admin_site = AdminSite(name='my_admin')
admin_site.site_header_color = '#FF0000'  # Replace with your desired color value

urlpatterns = [
    # ... other URL patterns ...
    path('admin/', admin_site.urls),
]
urlpatterns = [
    path('', views.index, name="home"),
    path('ulogin/', views.ulogin, name="ulogin"),
    path('ulogout/', views.ulogout, name="ulogout"),
    path('signup/', views.signup, name="singup"),
    path('contact/', views.contact, name="contact"),
    path('myprofile/', views.myprofile, name="myprofile"),
    path('creatcom/', views.creatcom, name="creatcom"),
    path('viewcom/', views.viewcom, name="viewcom"),
    path('feedback1/', views.feedback1, name="feedback"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

