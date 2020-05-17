from django.urls import path
from app.item import views

urlpatterns = [
    path('add/<int:container_pk>', views.ItemAddFormView.as_view(), name='item_add_form'),
    path('edit/<int:container_pk>/<int:pk>', views.ItemEditFormView.as_view(), name='item_edit_form'),
]
