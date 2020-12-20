from django.urls import path

from . import views

app_name = 'parse'
urlpatterns = [
    path('', views.index, name='index'),
    path('validasi', views.validasi, name='validasi'),
    path('get/kalimat', views.getKalimat, name='getKalimat'),
]
