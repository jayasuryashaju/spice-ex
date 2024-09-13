from django.db import models
import os
import uuid

# Create your models here.

def generate_unique_filename(instance, filename):
    ext = os.path.splitext(filename)[1]  # Extract the file extension
    filename_base = f"{uuid.uuid4().hex}"  # Generate a unique base using UUID
    unique_filename = f"{filename_base}{ext}"  # Combine with extension
    return os.path.join(instance.__class__.__name__.lower(), unique_filename)

class Banner(models.Model):
    title = models.CharField(max_length=255)
    subheading = models.CharField(max_length=255, blank=True)
    background_image = models.ImageField(upload_to='banners/')
    overlay_opacity = models.FloatField(default=0.5)  # Overlay opacity (optional)
    button_text = models.CharField(max_length=50, default="View Details")
    button_link = models.URLField(default="#", blank=True)

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"

    def __str__(self):
        return self.title


