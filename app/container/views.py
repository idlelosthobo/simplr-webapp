from django.shortcuts import render, reverse
from django.views import generic
from app.container import models
from app.container import forms


class ContainerListView(generic.ListView):
    model = models.Container
    template_name = 'container/container_list_view_page.html'


class ContainerAddFormView(generic.CreateView):

    model = models.Container
    form_class = forms.ContainerAddForm
    template_name = 'core/page_form.html'

    def get_success_url(self):
        return reverse('container_list_view')