"""
  All app views.
"""

from django.shortcuts import render

def index(request):
    """
      Test func.
    """
    return render(request, 'pages/index.html')

def about(request):
    """
      Test func.
    """
    return render(request, 'pages/about.html')

def login(request):
    """
      Test func.
    """
    return render(request, 'pages/login.html')

def register(request):
    """
      Test func.
    """
    return render(request, 'pages/register.html')
