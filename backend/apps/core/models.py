from django.db import models



class Basemodel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    update_time = models.DateTimeField(auto_now=True, editable=False, null=True)
    created_by = models.ForeignKey(
        "authentication.Usermodel", models.SET_NULL, null=True, blank=True, related_name="%(app_label)s_created_%(class)s"
    )
    update_by = models.ForeignKey(
        "authentication.Usermodel", models.SET_NULL, null=True, blank=True, related_name="%(app_label)s_updated_%(class)s"
    )
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ("id",)
