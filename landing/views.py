"""
Imports:
- render
- base View class
"""
from django.shortcuts import render
from django.views import View


class Index(View):
    """
    Importing http methods from the View class
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')
