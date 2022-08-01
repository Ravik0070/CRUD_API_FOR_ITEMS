from django.db import models

class Item(models.Model):
    category = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    item_desc = models.TextField()
    item_price = models.IntegerField(default=0)
    item_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name