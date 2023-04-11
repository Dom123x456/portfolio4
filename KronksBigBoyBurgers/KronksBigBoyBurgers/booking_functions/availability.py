import datetime
from restaurant.models import Table, RestaurantBooking

def check_availability(Table, check_in, check_out):
    