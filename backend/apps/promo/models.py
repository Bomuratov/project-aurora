from django.db import models
from promo.utils.currency import CURRENCY, UZS
from core import get_basemodel 


Basemodel = get_basemodel()


class Promo(Basemodel):
    restaurant = models.ForeignKey("restaurant.Restaurant", on_delete=models.CASCADE, null=True, blank=True, related_name="restaurant")
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField()
    currency = models.CharField(choices=CURRENCY, default=UZS)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'promo'
        ordering = ["id"]