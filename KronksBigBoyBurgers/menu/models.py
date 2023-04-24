from django.db import models

# Create your models here.

class MenuItem(models.Model):
    CATEGORY_CHOICES = (
        ('burger', 'Burger'),
        ('side', 'Side'),
        ('drink', 'Drink'),
    
    from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = (
        ('burger', 'Burger'),
        ('side', 'Side'),
        ('drink', 'Drink'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)

    def __str__(self):
        return self.name
