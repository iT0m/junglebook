from django.db import models

# Create your models here.
from django.urls import reverse

class ShopManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().all
        )

class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)

    class Meta:
        ordering=['name']
        verbose_name_plural='categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse(
            'shop:product_list_by_category', args=[self.slug]
        )

class Product(models.Model):
    products=ShopManager
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    image=models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    class Meta:
        ordering=['name']
        indexes=[
            models.Index(fields=['id','slug'])
            ]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id])