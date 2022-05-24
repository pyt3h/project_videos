from django.db import models

# Create your models here.
class Brand(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self): return self.name

class Product(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/images/product')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)

    def __str__(self): return self.name

class Order(models.Model):
    class OrderStatus:
        PENDING = 0
        DELIVERED = 1
        CANCELED = 2

    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    
    qty = models.IntegerField()
    price_unit = models.IntegerField()
    total = models.IntegerField()

    order_date = models.DateTimeField()
    deliver_date = models.DateTimeField(blank=True, null=True)

    status = models.IntegerField()