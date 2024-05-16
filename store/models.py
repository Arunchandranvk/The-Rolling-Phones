from django.db import models
from accounts.models import *

# Create your models here.

class Profile(models.Model):
    image=models.ImageField(upload_to="profile_pic",null=True)
    user=models.OneToOneField(CustUser,on_delete=models.CASCADE,related_name="p_pic",null=True)
   

class Product(models.Model):
    productname=models.CharField(max_length=200)
    image=models.FileField(upload_to="product_image")    
    model=models.CharField(max_length=100)    
    ram=models.IntegerField()
    rom=models.IntegerField()
    battery=models.CharField(max_length=50,null=True)
    warranty=models.CharField(max_length=50)
    datetime=models.DateTimeField(auto_now_add=True)
    description=models.TextField(max_length=500,null=True)
    orginalprice=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name="p_user")
    category= models.ForeignKey(Category,on_delete=models.CASCADE,related_name='c_product',null=True)


class Laptop(models.Model):
    productname=models.CharField(max_length=200)
    image=models.FileField(upload_to="product_image")    
    model=models.CharField(max_length=100) 
    o_ram=(
        ('4GB','4GB'),
        ('8GB','8GB'),
        ('12GB','12GB'),
        ('16GB','16GB'),
        ('24GB','24GB'),
        ('32GB','32GB'),
    )   
    ram=models.CharField(max_length=20,choices=o_ram,default='8GB')
    disk=(
        ('HDD','HDD'),
        ('SSD','SSD')
    )
    hard_disk=models.CharField(max_length=50,choices=disk,default="SSD")
    rom=models.CharField(max_length=20)
    # type=models.CharField(max_length=50,null=True)
    processor=models.CharField(max_length=100)
    gen=(
        ('7th Gen','7th Gen'),
        ('8th Gen','8th Gen'),
        ('9th Gen','9th Gen'),
        ('10th Gen','10th Gen'),
        ('11th Gen','11th Gen'),
        ('12th Gen','12th Gen'),
        ('13th Gen','13th Gen')
    )
    generation =models.CharField(max_length=20,choices=gen,default="12th Gen")
    graphic_card=models.CharField(max_length=100)
    options=(
        ('Windows 7','Windows 7'),
        ('Windows 8','Windows 8'),
        ('Windows 10','Windows 10'),
        ('Windows 11','Windows 11'),
        ('Windows 12','Windows 12'),
        ('Ubantu','Ubantu'),
        ('Linux','Linux'),
    )
    operating_system=models.CharField(max_length=100,choices=options,default="Windows 12")
    size=(
        ('11.6 inch','11.6 inch'),
        ('12 inch','12 inch'),
        ('13.3 inch','13.3 inch'),
        ('14 inch','14 inch'),
        ('15.6 inch','15.6 inch'),
        ('17 inch','17 inch'),
    )
    screensize=models.CharField(max_length=100,choices=size,default="15.6 inch")
    warranty=models.CharField(max_length=50)
    datetime=models.DateTimeField(auto_now_add=True)
    description=models.TextField(max_length=500,null=True)
    orginalprice=models.IntegerField(null=True)
    price=models.IntegerField(null=True)
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name="l_user")
    category= models.ForeignKey(Category,on_delete=models.CASCADE,related_name='c_l',null=True)


class Item_FFTH(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="items")
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='item_images',blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField()
    quantity=models.IntegerField()
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name="items")
    datetime=models.DateTimeField(auto_now_add=True)


class Books(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="a_cat")
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    img=models.ImageField(upload_to='item_images',blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField()
    quantity=models.IntegerField()
    user=models.ForeignKey(CustUser,on_delete=models.CASCADE,related_name="a_user")
    datetime=models.DateTimeField(auto_now_add=True)
