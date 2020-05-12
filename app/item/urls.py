from django.urls import path
from app.core import views

urlpatterns = [
    path('new/', views.home, name='something_home'),
]
