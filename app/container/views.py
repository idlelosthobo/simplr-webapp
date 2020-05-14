from django.shortcuts import render, reverse
from django.views import generic
from app.container import models
from app.container import forms


class ContainerListView(generic.TemplateView):

    template_name = 'container/container_list_view_page.html'

    # def get_queryset(self):
    #     if 'container_pk' in self.kwargs:
    #         if self.kwargs['container_pk'] != 0:
    #             container = models.Container.objects.filter(parent_id=self.kwargs['container_pk'])
    #         else:
    #             container = models.Container.objects.filter(parent=None)
    #     else:
    #         container = models.Container.objects.filter(parent=None)
    #     return container

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'container_pk' in self.kwargs:
            if self.kwargs['container_pk'] != 0:
                container = models.Container.objects.get(pk=self.kwargs['container_pk'])
                context['container'] = container
                context['container_list'] = models.Container.objects.filter(parent_id=self.kwargs['container_pk'])
                if container.parent:
                    context['bread_crumb'] = container.parent.name + ' > ' + container.name
                else:
                    context['bread_crumb'] = 'Home > ' + container.name
            else:
                context['container_list'] = models.Container.objects.filter(parent=None)
                context['bread_crumb'] = 'Home'
        else:
            context['container_list'] = models.Container.objects.filter(parent=None)
            context['bread_crumb'] = 'Home'
        return context


class ContainerAddFormView(generic.CreateView):

    model = models.Container
    form_class = forms.ContainerAddForm
    template_name = 'core/page_form.html'

    def get_success_url(self):
        return reverse('container_list_view', kwargs={'container_pk':0})