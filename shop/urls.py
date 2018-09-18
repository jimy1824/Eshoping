from django.urls import path
from .views import *
urlpatterns = [
    path('shop/', Shop.as_view(),
         name='shop'),
    path('product/', Product.as_view(),
         name='product'),
    path('cart/', Cart.as_view(),
         name='cart'),
]