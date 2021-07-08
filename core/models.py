from django.db import models

# Create your models here.
class ShippingLabel(models.Model):
    customer_name = models.CharField(max_length=500)
    phone_number = models.BigIntegerField()
    falt_house_no_building_name = models.TextField()
    street_colony = models.TextField()
    pincode = models.CharField(max_length=6)
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    landmark = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.customer_name}'