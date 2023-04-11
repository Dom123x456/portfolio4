from django.contrib import admin
from .models import TableCategory, RestaurantBooking

# Register your models here.
admin.site.register(TableCategory)
admin.site.register(RestaurantBooking)