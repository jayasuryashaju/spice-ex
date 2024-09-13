from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext as _
import os
import uuid

def generate_unique_filename(instance, filename):
    ext = os.path.splitext(filename)[1]  # Extract the file extension
    filename_base = f"{uuid.uuid4().hex}"  # Generate a unique base using UUID
    unique_filename = f"{filename_base}{ext}"  # Combine with extension
    return os.path.join(instance.__class__.__name__.lower(), unique_filename)

class Category(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'))
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, max_length=255, editable=False)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=generate_unique_filename, blank=True)
    has_offer = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        

class Product(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, 'Delete'))
    
    name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    additional_description = models.TextField(blank=True)
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    slug = models.SlugField(unique=True, max_length=255, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    has_offer = models.BooleanField(default=False)
    offer_details = models.TextField(blank=True, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # New price field
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=None)  # New offer price field
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name  
    
    def get_absolute_url(self):
        return reverse('store:product_details', args=[self.slug])
    
    def get_related_products(self, num_related=10):
        current_product_categories = [self.category]
        related_products = Product.objects.filter(
            category__in=current_product_categories
        ).exclude(id=self.id).distinct()[:num_related]
        return related_products

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def parse_offer_details(self, offer_details_text):
        details = {}
        for item in offer_details_text.split('\n'):
            if item.strip():
                key, value = item.split(':', 1)
                details[key.strip()] = value.strip()
        return details


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')  
    alt_text = models.CharField(max_length=255, blank=True)
    is_featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)



