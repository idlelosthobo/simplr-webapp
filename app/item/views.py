from django.shortcuts import render, reverse
from django.views import generic
from app.item import forms, models


# Create your views here.
class ItemAddFormView(generic.CreateView):

    model = models.Item
    form_class = forms.ItemAddForm
    template_name = 'core/page_form.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        if self.kwargs['container_pk'] != 0:
            form.instance.container_id = self.kwargs['container_pk']
        return super(ItemAddFormView, self).form_valid(form)

    def get_success_url(self):
        return reverse('container_list_view', kwargs={'container_pk':self.kwargs['container_pk']})


class ItemEditFormView(generic.UpdateView):

    model = models.Item
    form_class = forms.ItemEditForm
    template_name = 'core/page_form.html'

    def get_success_url(self):
        return reverse('container_list_view', kwargs={'container_pk': self.kwargs['container_pk']})