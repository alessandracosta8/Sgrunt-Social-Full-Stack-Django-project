""" Imports """
from django.shortcuts import render


def page_not_found_view(request, exception):
    """ 404 customer error view """
    return render(request, '404.html', status=404)
