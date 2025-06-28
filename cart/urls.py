from django.urls import path
from . import views

urlpatterns = [
    path('api/cart/', views.cart_api, name='cart-api'),
    path('api/cart/add/<int:product_id>/', views.add_to_cart, name='add-to-cart'),
    path('api/cart/update/<int:product_id>/', views.update_cart_item, name='update-cart-item'),
    path('api/cart/remove/<int:product_id>/', views.remove_cart_item, name='remove-cart-item'),
]