from django.db import models
from django.conf import settings
from django.urls import reverse_lazy

# Create your models here.

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f'Table {self.table_number}'


class TableCategory(models.Model):
    title = models.CharField(max_length=50)

    STANDARD = 'Standard'
    DELUXE = 'Deluxe'

    CATEGORY_CHOICES = [
        (STANDARD, 'Standard'),
        (DELUXE, 'Deluxe'),
    ]

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

class RestaurantBooking(models.Model):
    PAYMENT_STATUSES = (
        ('COM', 'PAYMENT_COMPLETE'),
        ('INC', 'PAYMENT_INCOMPLETE'),
        ('PAR', 'PAYMENT_PARTIALLY_COMPLETE'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_start = models.DateTimeField()
    reservation_end = models.DateTimeField()
    payment_status = models.CharField(max_length=3, choices=PAYMENT_STATUSES)

    def __str__(self):
        return f'From = {self.reservation_start.strftime("%d-%b-%Y %H:%M")} To = {self.reservation_end.strftime("%d-%b-%Y %H:%M")}'
