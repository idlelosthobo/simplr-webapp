from django.urls import path
from app.container import views

urlpatterns = [
    path('add/', views.ContainerAddFormView.as_view(), name='container_add_form'),
    path('all/', views.ContainerListView.as_view(), name='container_list_view')
]
