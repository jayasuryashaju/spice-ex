from product.models import Category, Product

def categories_and_products_context(request):
    categories = Category.objects.filter(delete_status=Category.LIVE)
    products = Product.objects.filter(delete_status=Product.LIVE)
    return {
        'categories': categories,
        'products': products,
    }
    print(categories)