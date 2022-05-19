from distutils.command.upload import upload
from email.mime import image
from operator import truediv
from pydoc import describe
from django.db import models

# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
    
class Products(models.Model):
    name=models.CharField(max_length=200)
    image1=models.ImageField(upload_to='photos/%y/%m/%d')
    image2=models.ImageField(upload_to='photos/%y/%m/%d')
    image3=models.ImageField(upload_to='photos/%y/%m/%d')
    price=models.DecimalField(max_digits=10,decimal_places=3)
    description=models.TextField()
    catego=models.ForeignKey(Categories,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(null=True)
    orderd=models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
Products.objects.order_by("timestamp")