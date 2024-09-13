from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from store.models import Banner
from product.models import Product, Category
from django.core.paginator import Paginator



def home(request):
    title = "Home"
    banners = Banner.objects.all()

    context = {
        'title': title,
        'banners': banners,
    }

    return render(request, 'index.html', context)

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug, delete_status=Product.LIVE)
    related_products = product.get_related_products()
    
    title = f"{product.name}"
    
    context = {
        'title': title,
        'product': product,
        'related_products': related_products,
    }
    
    return render(request, 'product_details.html', context)

def category_list(request, slug=None):
    if slug:
        # Get the category based on the slug
        category = get_object_or_404(Category, slug=slug, delete_status=Category.LIVE)
        # Filter products by the category
        products = Product.objects.filter(category=category, delete_status=Product.LIVE)
        title = category.name
    else:
        # If no slug is provided, show all products
        products = Product.objects.filter(delete_status=Product.LIVE)
        title = "All Products"
        category = None

    # Paginate the products list (e.g., 8 products per page)
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'title': title,
        'category': category,
        'page_obj': page_obj,
        'products': page_obj.object_list,
    }
    
    return render(request, 'category_list.html', context)



def about(request):
    title = "About Spice-EX"

    context = {
        'title': title,
    }

    return render(request, 'about.html', context)