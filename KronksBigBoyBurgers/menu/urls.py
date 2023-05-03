from menu import views
from django.urls import path, include

urlpatterns = [
    path('', views.menus, name='menu'),
    path('food_menu', views.FoodMenu.as_view(), name='food_menu'),
    path('drinks_menu', views.DrinksMenu.as_view(), name='drinks_menu'),
    path('menu/edit/', views.edit_menu_item, name='edit_menu_item'),
    path('menu/edit/<int:item_id>/', views.edit_menu_item, name='edit_menu_item_edit'),
]
