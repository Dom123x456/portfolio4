import datetime
from restaurant.models import Table, RestaurantBooking

def check_table_availability(table, reservation_start, reservation_end):
