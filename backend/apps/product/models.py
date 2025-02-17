from django.db import models
from core import utils, get_basemodel
from apps.product.utils.currency import CURRENCY, UZS

Basemodel = get_basemodel()


class Category(Basemodel):
    restaurant = models.ForeignKey(
        "restaurant.Restaurant", on_delete=models.CASCADE, null=True, blank=True, related_name="category_apps"
    )
    name = models.CharField(max_length=225)
    order = models.IntegerField(default=0)

    class Meta:
        db_table = 'product_category'
        ordering = ["order"]
    
    def __str__(self):
        return self.name



class Menu(Basemodel):
    name = models.CharField(max_length=225, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=100, choices=CURRENCY, default=UZS)
    photo = models.FileField(blank=True, upload_to=utils.upload_path_menu, null=True)
    availability = models.BooleanField(default=True)
    category = models.ForeignKey(
        "product.Category",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="category",
    )
    restaurant = models.ForeignKey(
        "restaurant.Restaurant", on_delete=models.CASCADE, null=True, blank=True, related_name="menu_apps"
    )

    class Meta:
        db_table = 'product_menu'

    def __str__(self):
        return f"{self.name}"
    
