from django.db import models

# Create your models here.

class MenuItem(models.Model):
    CATEGORY_CHOICES = (
        ('burger', 'Burger'),
        ('side', 'Side'),
        ('drink', 'Drink'),
    