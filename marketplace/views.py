from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from marketplace.models import Cart
from menu.models import Category, FoodItem
from vendors.models import Vendor
from django.db.models import Prefetch
from .context_processors import get_cart_counter, get_cart_amounts


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

    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
    else:
        cart_items = None

    context = {
        'vendor': vendor,
        'categories': categories,
        'cart_items': cart_items,
    }

    return render(request, 'marketplace/vendor_detail.html', context)


def addToCart(request, food_id):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Check if the food item exists
            try:
                fooditem = FoodItem.objects.get(id=food_id)
                # Check if the user has already added that food to the cart
                try:
                    checkCart = Cart.objects.get(user=request.user, fooditem=fooditem)
                    # Increase the cart quantity
                    checkCart.quantity += 1
                    checkCart.save()
                    return JsonResponse({'status': 'Success', 'message': 'Cantidad incrementada en el carrito', 'cart_counter': get_cart_counter(request), 'qty': checkCart.quantity, 'cart_amount': get_cart_amounts(request)})
                except:
                    checkCart = Cart.objects.create(user=request.user, fooditem=fooditem, quantity=1)
                    return JsonResponse({'status': 'Success', 'message': 'Ítem añadido al carrito', 'cart_counter': get_cart_counter(request), 'qty': checkCart.quantity, 'cart_amount': get_cart_amounts(request)})
            except:
                return JsonResponse({'status': 'Failed', 'message': '¡Este ítem no existe!'})
        else:
            return JsonResponse({'status': 'Failed', 'message': '¡Solicitud no válida!'})
    else:
        return JsonResponse({'status': 'login_required', 'message': 'Por favor inicia sesión para continuar'})


def decreaseCart(request, food_id):
    if request.user.is_authenticated:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Check if the food item exists
            try:
                fooditem = FoodItem.objects.get(id=food_id)
                # Check if the user has already added that food to the cart
                try:
                    checkCart = Cart.objects.get(user=request.user, fooditem=fooditem)
                    if checkCart.quantity > 1:
                        # decrease the cart quantity
                        checkCart.quantity -= 1
                        checkCart.save()
                    else:
                        checkCart.delete()
                        checkCart.quantity = 0
                    return JsonResponse({'status': 'Success', 'cart_counter': get_cart_counter(request), 'qty': checkCart.quantity, 'cart_amount': get_cart_amounts(request)})
                except:
                    return JsonResponse({'status': 'Failed', 'message': '¡No tienes este ítem en tu carrito!'})
            except:
                return JsonResponse({'status': 'Failed', 'message': '¡Este ítem no existe!'})
        else:
            return JsonResponse({'status': 'Failed', 'message': '¡Solicitud inválida!'})
        
    else:
        return JsonResponse({'status': 'login_required', 'message': '¡Por favor inicia sesión para continuar!'})


def cart(request):
    cart_items = Cart.objects.filter(user=request.user)

    context = {
        'cart_items': cart_items,
    }

    return render(request, 'marketplace/cart.html', context)