""" Imports """
from django.shortcuts import render


def page_not_found_view(request, exception):
    """ 404 """
    return render(request, '404.html')
