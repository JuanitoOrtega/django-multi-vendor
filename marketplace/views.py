from django.shortcuts import render, get_object_or_404
from menu.models import Category, FoodItem
from vendors.models import Vendor
from django.db.models import Prefetch


def marketplace(request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)
    vendor_count = vendors.count()
    
    context = {
        'vendors': vendors,
        'vendor_count': vendor_count,
    }

    return render(request, 'marketplace/listings.html', context)


def vendorDetail(request, slug):
    vendor = get_object_or_404(Vendor, slug=slug)
    categories = Category.objects.filter(vendor=vendor).prefetch_related(
        Prefetch(
            'fooditems',
            queryset = FoodItem.objects.filter(is_available=True)
        )
    )

    context = {
        'vendor': vendor,
        'categories': categories,
    }

    return render(request, 'marketplace/vendor_detail.html', context)
