from django.urls import path

from .views import *

urlpatterns = [
    path('save-order', save_order),
    path('confirm-order/<pk>', confirm_order),
    path('cancel-order/<pk>', cancel_order),
    path('search-order', search_order),
    path('get-order-by-id/<pk>', get_order_by_id),
    path('get-all-brand', get_all_brand),
    path('search-product', search_product),
    path('get-product-by-id/<pk>', get_product_by_id),
    path('hello', hello)
]
