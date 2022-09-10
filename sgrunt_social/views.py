""" Imports """
from django.conf import settings
from django.shortcuts import redirect


def error_404_view(request, exception):
    """ handler of 404 errors """
    return render(request, '404.html')
