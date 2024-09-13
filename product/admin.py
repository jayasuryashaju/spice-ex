from django import forms
from django.db import models 
from django.contrib import admin
from .models import Category, Product, ProductImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_offer', 'is_featured')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)



class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name', 'category', 'price', 'offer_price', 'is_featured', 'has_offer', 'date_created')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'is_featured', 'has_offer')  # Add list filters for better admin filtering
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 4, 'cols': 40})},
    }
    readonly_fields = ('slug',)  # Make the slug field read-only in the admin

    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'description', 'additional_description', 'price', 'offer_price', 'is_featured', 'has_offer', 'offer_details', 'stock')
        }),
        ('Metadata', {
            'fields': ('slug', 'date_created', 'date_modified')
        }),
    )
    readonly_fields = ('slug', 'date_created', 'date_modified')  # Keep slug, date_created, and date_modified read-only

admin.site.register(Product, ProductAdmin)
