from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('product/',views.Product_register,name="product"),
    path('product_list/',views.Product_list,name="product_list"),
]