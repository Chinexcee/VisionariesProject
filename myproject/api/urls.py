from django.urls import path
from . import views

urlpatterns = [
    # Category URLs
    path('categories/', views.category_list_create, name='category-list-create'),
    path('categories/<int:pk>/', views.category_detail, name='category-detail'),
    
    # SubCategory URLs
    path('subcategories/', views.subcategory_list_create, name='subcategory-list-create'),
    path('subcategories/<int:pk>/', views.subcategory_detail, name='subcategory-detail'),
    
    # Product URLs
    path('products/', views.product_list_create, name='product-list-create'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
]
