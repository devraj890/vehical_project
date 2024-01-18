from django.urls import path
from .import views


urlpatterns = [
    path('', views.plogin, name="plogin"),
    path('phome/', views.phome, name="phome"),
    path('found/', views.found, name="found"),
    path('plogout/', views.plogout, name="plogout"),
]