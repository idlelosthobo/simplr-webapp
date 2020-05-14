from django.shortcuts import render, reverse
from django.views import generic
from app.item import forms, models


# Create your views here.
class ItemAddFormView(generic.CreateView):

    model = models.Item
    form_class = forms.ItemAddForm
    template_name = 'core/page_form.html'

    def get_success_url(self):
        return reverse('container_list_view', kwargs={'container_pk':0})