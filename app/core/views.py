from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import permission_required


@permission_required('core.view_home')
def home(response):
    return render(request=response, template_name='home.html')
    # return render(response, "core/page.html", {})
