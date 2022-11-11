from django.urls import path
from .import views


urlpatterns = [
    path('',views.home, name='home'),
    path('product/',views.product, name='product'),
    path('accessories/',views.accessories, name='accessories'),
    path('fashion/',views.fashion, name='fashion'),
    path('electronic/',views.electronic, name='electronic'),
    path('cart/',views.cart, name='cart'),
]
