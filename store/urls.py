# store/urls.py
from django.urls import path
from . import views
app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('product_details/<slug:slug>', views.product_details, name='product_details'),
    path('category_all/', views.category_list, name='category_all'),
    path('category_list/<slug:slug>/', views.category_list, name='category_list'),
    path('about/', views.about, name='about'),

]
