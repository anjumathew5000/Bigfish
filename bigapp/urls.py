from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('product/',views.Product_register,name="product"),
    path('product/<int:product_id>',views.Product_register,name="product"),
    path('product_list/',views.Product_list,name="product_list"),
    path('product_delete/<int:product_id>',views.product_delete,name="product_delete"),
    path('product_edit/<int:product_id>',views.product_edit,name="product_edit"),
]
