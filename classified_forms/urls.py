from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "classified"

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
    path('next-of-kin/', views.next_kin, name='next_kin'),

    
    
    # path('', include('classified_forms.urls')),

]
