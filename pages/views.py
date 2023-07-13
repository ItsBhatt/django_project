"""
  All app views.
"""

# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """
      Test func.
    """
    return HttpResponse('<h1>Hello World</h1>')
