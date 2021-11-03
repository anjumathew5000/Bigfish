from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50,null=True)
    product_category=models.CharField(max_length=50,null=True)
    product_rate=models.IntegerField()
    product_details=models.CharField(max_length=200,null=True)
    product_stoke=models.IntegerField()

     