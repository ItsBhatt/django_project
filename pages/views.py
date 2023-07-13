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
