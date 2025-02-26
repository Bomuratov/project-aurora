from django.db import models
from core import utils, get_basemodel

BaseModel = get_basemodel()

class Restaurant(BaseModel):
    admin = models.ForeignKey("authentication.UserModel", on_delete=models.SET_NULL, null=True, blank=True)
    editors = models.ManyToManyField("authentication.UserModel", blank=True, related_name="editors")
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    telegram_link = models.CharField(max_length=225)
    instagram_link = models.CharField(max_length=225)
    orders = models.BooleanField(default=False)
    waiter = models.BooleanField(default=False)
    background_photo = models.ImageField(upload_to=utils.upload_path_vendor_backgroud)
    logo = models.ImageField(upload_to=utils.upload_path_vendor_logo)
    orders_chat_id = models.BigIntegerField(null=True, blank=True) 
    waiter_chat_id = models.BigIntegerField(null=True, blank=True)
    stir = models.BigIntegerField(null=True, blank=True)
    legal_name = models.CharField(max_length=255, null=True, blank=True)
    legal_address = models.CharField(max_length=255, null=True, blank=True)
    contact_entity = models.CharField(max_length=255, null=True, blank=True, validators=[utils.UZB_PHONE_VALIDATOR])
    contact_support = models.CharField(max_length=255, null=True, blank=True, validators=[utils.UZB_PHONE_VALIDATOR])




    def __str__(self):
        return self.name
    
