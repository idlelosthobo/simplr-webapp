from django.urls import path
from app.container import views

urlpatterns = [
    path('add/', views.ContainerAddFormView.as_view(), name='container_add_form'),
    path('view/<int:container_pk>/', views.ContainerListView.as_view(), name='container_list_view')
]
