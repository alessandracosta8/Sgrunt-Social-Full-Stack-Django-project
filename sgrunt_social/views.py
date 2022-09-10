""" Imports """
from django.shortcuts import render


def page_not_found_view(request, exception):
    """ error 404 handler """
    return render(request, 'not_found.html')


def server_error(request):
    """ error 500 handler """
    return render(request, 'server_error.html')