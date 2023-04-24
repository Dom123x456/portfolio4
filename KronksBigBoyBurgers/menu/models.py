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

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)

    def __str__(self):
        return self.name
