from django.db import models

class ProductManager(models.Manager):
    def get_available_products(self):
        return self.filter(quantity__gt=0)
