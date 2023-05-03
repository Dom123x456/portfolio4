from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import MenuItem, FoodItem, DrinkItem
from django.contrib.auth.decorators import login_required
from .forms import MenuItemForm
from django.core.paginator import Paginator

def menu(request):
    search_query = request.GET.get('search', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    dietary = request.GET.get('dietary', '')
    allergens = request.GET.get('allergens', '')

    # Filter menu items based on the search criteria
    items = MenuItem.objects.filter(on_menu=True)

    if search_query:
        items = items.filter(item_name__icontains=search_query)

    if min_price:
        items = items.filter(price__gte=min_price)

    if max_price:
        items = items.filter(price__lte=max_price)

    if dietary:
        items = items.filter(dietary__icontains=dietary)

    if allergens:
        items = items.filter(allergens__icontains=allergens)

    # Get all food items and drinks items separately
    food_items = MenuItem.objects.filter(item_type=0, on_menu=True)
    drink_items = MenuItem.objects.filter(item_type=1, on_menu=True)

    # Group food and drinks items by their menu section
    food_items_by_section = {}
    drink_items_by_section = {}

    for section, name in MenuItem.MENU_SECTION_CHOICES:
        food_items_by_section[name] = food_items.filter(menu_section=section)
        drink_items_by_section[name] = drink_items.filter(menu_section=section)

    # Pagination
    paginator = Paginator(items, 10)  # Show 10 items per page
    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'items': items,
        'food_items_by_section': food_items_by_section,
        'drink_items_by_section': drink_items_by_section,
    }

    return render(request, 'menu.html', context)

