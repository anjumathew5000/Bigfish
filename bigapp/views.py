from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def Product_register(request):
    return render(request,'product_add.html')
def Product_list(request):
    return render(request,'produc_list.html')