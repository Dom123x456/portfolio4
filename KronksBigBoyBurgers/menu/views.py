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

class FoodMenu(generic.ListView):
    """
    Render food menus as a list of items from the database
    """
    model = FoodItem
    template_name = 'food_menu.html'
    context_object_name = 'food_items'

    def get_queryset(self):
        queryset = FoodItem.objects.filter(on_menu=True)
        return queryset


class DrinksMenu(generic.ListView):
    """
    Render drinks menus as a list of items from the database
    """
    model = DrinkItem
    template_name = 'drinks_menu.html'
    context_object_name = 'drinks_items'

    def get_queryset(self):
        queryset = {
            'hot_drinks': DrinkItem.objects.filter(on_menu=True, drinks_menu_section=0),
            'kids_drinks': DrinkItem.objects.filter(on_menu=True, drinks_menu_section=1),
            'beverages_alcohol': DrinkItem.objects.filter(on_menu=True, drinks_menu_section=2)
        }
        return queryset

@login_required
def edit_menu_item(request, item_id=None):
    if item_id:
        menu_item = get_object_or_404(MenuItem, item_id=item_id)
    else:
        menu_item = MenuItem()

    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            return redirect('menus')
    else:
        form = MenuItemForm(instance=menu_item)

    context = {
        'form': form,
        'menu_item': menu_item,
    }

    