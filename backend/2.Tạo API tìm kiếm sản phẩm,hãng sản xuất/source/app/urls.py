from django.urls import path

from .views import *

urlpatterns = [
    path('get-all-brand', get_all_brand),
    path('search-product', search_product),
    path('get-product-by-id/<pk>', get_product_by_id),
    path('hello', hello)
]
