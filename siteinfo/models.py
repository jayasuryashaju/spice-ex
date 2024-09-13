from django.db import models
import os
import uuid

# Create your models here.

def generate_unique_filename(instance, filename):
    ext = os.path.splitext(filename)[1]  # Extract the file extension
    filename_base = f"{uuid.uuid4().hex}"  # Generate a unique base using UUID
    unique_filename = f"{filename_base}{ext}"  # Combine with extension
    return os.path.join(instance.__class__.__name__.lower(), unique_filename)

class SiteInfo(models.Model):
    site_name = models.CharField(max_length=255, default="SpiceEx")
    logo = models.ImageField(upload_to='siteinfo/', blank=True, null=True)  # Main logo
    small_logo = models.ImageField(upload_to='siteinfo/', blank=True, null=True)  # Small logo for tabs (favicon)
    
    class Meta:
        verbose_name = "Site Information"
        verbose_name_plural = "Site Information"

    def __str__(self):
        return self.site_name

class Address(models.Model):
    site_info = models.ForeignKey(SiteInfo, on_delete=models.CASCADE, related_name='addresses')
    address = models.TextField()

    def __str__(self):
        return self.address

class Email(models.Model):
    site_info = models.ForeignKey(SiteInfo, on_delete=models.CASCADE, related_name='emails')
    email = models.EmailField()

    def __str__(self):
        return self.email

class PhoneNumber(models.Model):
    site_info = models.ForeignKey(SiteInfo, on_delete=models.CASCADE, related_name='phone_numbers')
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.phone_number
    
class WhatsAppPhoneNumber(models.Model):
    site_info = models.ForeignKey(SiteInfo, on_delete=models.CASCADE, related_name='whatsapp_phone_number')
    whatsapp_phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.whatsapp_phone_number


class SocialMediaLink(models.Model):
    site_info = models.ForeignKey(SiteInfo, on_delete=models.CASCADE, related_name='social_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name



class About(models.Model):
    description = models.TextField(blank=True)

    def __str__(self):
        return self.description

class Specialities(models.Model):
    title = models.CharField(max_length=255)  # Title field
    image = models.ImageField(upload_to=generate_unique_filename)  # Image field with unique filename
    description = models.TextField(blank=True)  # Description field

    class Meta:
        verbose_name = "Speciality"
        verbose_name_plural = "Specialities"

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField(max_length=255)
    iframe_code = models.TextField()

    def __str__(self):
        return self.name