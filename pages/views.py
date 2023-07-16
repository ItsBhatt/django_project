"""
  All app views.
"""

from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor

def index(request):
    """
      Test func.
    """
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    context = {
        'listings': listings
    }

    return render(request, 'pages/index.html', context)

def about(request):
    """
      Test func.
    """
    realtors = Realtor.objects.order_by('hire_date').all()
    mvp = {}

    for realtor in realtors:
        if realtor.is_mvp:
            mvp = realtor
            break

    context = {
        'realtors': realtors,
        'mvp': mvp,
    }

    return render(request, 'pages/about.html', context)

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
