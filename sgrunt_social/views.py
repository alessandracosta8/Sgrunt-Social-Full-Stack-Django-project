""" Imports """
from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404(request, exception, template_name="404.html"):
    """ 404 handling """
    response = render_to_response(template_name)
    response.status_code = 404
    return response

def handler500(request, exception, template_name="500.html"):
    """ 500 handling """
    response = render_to_response(template_name)
    response.status_code = 500
    return response
