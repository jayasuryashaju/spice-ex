from django.contrib import admin
from .models import SiteInfo, Address, Email, PhoneNumber, SocialMediaLink, WhatsAppPhoneNumber, About, Specialities, Location

class AddressInline(admin.TabularInline):
    model = Address
    extra = 1
    fields = ('address',)  # Specify which fields to display in the inline

class EmailInline(admin.TabularInline):
    model = Email
    extra = 1
    fields = ('email',)

class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1
    fields = ('phone_number',)

class WhatsAppPhoneNumberInline(admin.TabularInline):
    model = WhatsAppPhoneNumber
    extra = 1
    fields = ('whatsapp_phone_number',)

class SocialMediaLinkInline(admin.TabularInline):
    model = SocialMediaLink
    extra = 1
    fields = ('name', 'url')

@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    inlines = [AddressInline, EmailInline, PhoneNumberInline, WhatsAppPhoneNumberInline, SocialMediaLinkInline]
    fields = ['site_name', 'logo', 'small_logo']
    list_display = ('site_name', 'logo', 'small_logo')  # Display these fields in the list view
    search_fields = ('site_name',)  # Add a search bar for site_name

class AboutAdmin(admin.ModelAdmin):
    list_display = ('description',)  # Display description in the list view
    search_fields = ('description',)  # Add a search bar for description

class SpecialitiesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_preview')  # Include image_preview in list display
    search_fields = ('title', 'description')  # Search bar for title and description
    list_filter = ('title',)  # Filter options by title
    readonly_fields = ('image_preview',)  # Display image preview

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" />'
        return ""
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'

# Register your models and custom admin configurations
admin.site.register(Location)
admin.site.register(About, AboutAdmin)
admin.site.register(Specialities, SpecialitiesAdmin)
