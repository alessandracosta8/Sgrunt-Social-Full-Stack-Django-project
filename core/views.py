""" Imports """
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """ index page url """
    return HttpResponse('<h1>Welcome to Sgrunt Social!</h1>')
