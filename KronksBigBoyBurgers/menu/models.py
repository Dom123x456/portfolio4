from django.db import models

# Create your models here.
ITEM_TYPE_CHOICES = ((0, "Food"), (1, "Drink"))

MENU_SECTION_CHOICES = (
    (0, "Burgers"),
    (1, "Sides"),
    (2, "Desserts"),
    (3, "Soft Drinks"),
    (4, "Shakes & Floats"),
    (5, "Beer"),
    (6, "Wine & Cocktails"),
    (7, "New Food Item"),
    (8, "New Drink Item"),
)
class MenuItem(models.Model):
    """
    Menu items model
    """
    item_id = models.AutoField(primary_key=True)
    item_type = models.IntegerField(choices=ITEM_TYPE_CHOICES)
    item_name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    dietary = models.CharField(max_length=200)
    allergens = models.CharField(max_length=200, null=True)
    menu_section = models.IntegerField(choices=MENU_SECTION_CHOICES)
    on_menu = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)