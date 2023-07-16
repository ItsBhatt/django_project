from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    listings = Listing.objects.filter(is_published = True).order_by('-list_date')
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)

    context = {
        'listings': paged_listing
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = Listing.objects.get(id = listing_id)
    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')
