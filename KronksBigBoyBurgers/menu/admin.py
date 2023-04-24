from django.contrib import admin
from .models import MenuItem

# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_filter = ('menu_section', 'price', 'item_type', 'on_menu')
    list_display = ('item_name', 'menu_section', 'price', 'item_type', 'on_menu')
