import datetime
from restaurant.models import Table, RestaurantBooking

def check_table_availability(table, reservation_start, reservation_end):
    availability = []
    reservations = RestaurantBooking.objects.filter(table=table)
    
    for reservation in reservations:
        if reservation.reservation_start > reservation_end or reservation.reservation_end < reservation_start:
            availability.append(True)
        else:
            availability.append(False)
    
    return all(availability)
