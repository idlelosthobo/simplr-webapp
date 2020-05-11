from django.urls import path, include
from django.views.generic import TemplateView
from app.registration import views
from app.core import views

urlpatterns = [
    path('', views.home, name='home'),
]
