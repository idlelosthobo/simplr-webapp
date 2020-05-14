from django.urls import path
from app.item import views

urlpatterns = [
    path('add/', views.ItemAddFormView.as_view(), name='item_add_form'),
]
