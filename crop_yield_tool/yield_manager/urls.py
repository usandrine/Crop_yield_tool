from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crop/<int:crop_id>/', views.crop_detail, name='crop_detail'),
]
