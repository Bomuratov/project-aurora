from django.db import models
from core import utils, get_basemodel

BaseModel = get_basemodel()

class Restaurant(BaseModel):
    user = models.ForeignKey("vendors.VendorModel", on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=225)
    adress = models.CharField(max_length=225)
    telegram_link = models.CharField(max_length=225)
    instagram_link = models.CharField(max_length=225)
    orders = models.BooleanField(default=False)
    waiter = models.BooleanField(default=False)
    backgroud_photo = models.ImageField(upload_to=utils.upload_path_vendor_backgroud)
    logo = models.ImageField(upload_to=utils.upload_path_vendor_logo)


    def __str__(self):
        return self.name

