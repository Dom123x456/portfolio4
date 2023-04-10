from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
# Create your models here.

class TableCategory(models.Model):
    title = models.CharField(max_length=50)

    STANDARD = 'Standard'
    DELUXE = 'Deluxe'

    CATEGORY_CHOICES = [
        (STANDARD, 'Standard'),
        (DELUXE, 'Deluxe'),
    ]

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
