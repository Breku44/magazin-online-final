from django.urls import path
from .views import home, product_list, add_to_cart, payment_confirmation, blog, announcement1, announcement2

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('pay_now/', payment_confirmation, name='pay_now'),
    path('blog/', blog, name='blog'),
    path('announcement1/', announcement1, name='announcement1'),
    path('announcement2/', announcement2, name='announcement2'),
]
