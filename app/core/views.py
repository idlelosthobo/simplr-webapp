from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import permission_required
from django.views import generic
from app.container.models import Container
from app.item.models import Item
from django.db.models import Q


@permission_required('core.view_home')
def home(response):
    return render(request=response, template_name='home/home.html')
    # return render(response, "core/page.html", {})


class SearchListView(generic.TemplateView):

    template_name = 'core/search/search_list_view_page.html'

    def get_context_data(self, **kwargs):
        context_data = super(SearchListView, self).get_context_data(**kwargs)
        query = self.request.GET.get('query')
        context_data['container_list'] = Container.objects.filter(
            Q(name__icontains=query)
        )
        context_data['item_list'] = Item.objects.filter(
            Q(name__icontains=query) | Q(data__icontains=query)
        )
        return context_data
