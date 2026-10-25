from django.db import models
from django.conf import settings
from products.models import Product




class Korzina(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='korzina'
    )
class KorzinaUpr(models.Model):
    korzina = models.ForeignKey(Korzina, on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)