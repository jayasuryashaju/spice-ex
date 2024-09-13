from .models import About, Specialities, SiteInfo, Location, WhatsAppPhoneNumber

def site_info_context(request):
    site_info = SiteInfo.objects.first()
    about = About.objects.first()  
    specialities = Specialities.objects.all()  
    location = Location.objects.first()  

    # Get the WhatsApp phone number
    whatsapp_number = site_info.whatsapp_phone_number.first() if site_info else None

    # Load social links by checking names
    social_links = {}
    if site_info:
        for link in site_info.social_links.all():
            social_links[link.name.lower()] = link.url  # Store links in a dictionary with lowercase names as keys

    return {
        'site_info': site_info,
        'addresses': site_info.addresses.all() if site_info else [],
        'emails': site_info.emails.all() if site_info else [],
        'phone_numbers': site_info.phone_numbers.all() if site_info else [],
        'whatsapp_number': whatsapp_number,  # Add WhatsApp number to context
        'social_links': social_links,  # Add social links as a dictionary
        'about': about,
        'specialities': specialities,
        'location': location,
    }
