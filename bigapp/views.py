from django.shortcuts import render,redirect
from bigapp.models import Product
# Create your views here.
def index(request):
    return render(request,'index.html')


def Product_register(request,product_id=None):
    if product_id:
        product=Product.objects.get(id=product_id)
        # if request.method =='POST':
        #     product_name=request.POST.get('pname')
        #     product_rate=request.POST.get('prate')
        #     product_stoke=request.POST.get('pstock')
        #     product_details=request.POST.get('pdetail')
        #     product_cateogory=request.POST.get('productcat')
        #     product.objects.filter(id=product_id).update(product_name=product_name,
        #                                     product_category=product_cateogory,
        #                                     product_rate=product_rate,
        #                                     product_details=product_details,
        #                                     product_stoke=product_stoke)
        #     return redirect(product_list)
     
        return render(request,'product_add.html',{'products':product})
        

    if request.method =='POST':
        print("hi")
        product_name=request.POST.get('pname')
        product_rate=request.POST.get('prate')
        product_stoke=request.POST.get('pstock')
        product_details=request.POST.get('pdetail')
        product_cateogory=request.POST.get('productcat')
        product=Product.objects.create(product_name=product_name,
                                    product_category=product_cateogory,
                                    product_rate=product_rate,
                                    product_details=product_details,
                                    product_stoke=product_stoke)
        product.save()
        context={"message":"sucsessfully registered"}
        return redirect(Product_list)
   
       
    return render(request,'product_add.html')

def Product_list(request):
    product_data=Product.objects.all()
    context={"products":product_data}
    return render(request,'produc_list.html',context)
def product_delete(request,product_id):
    product=Product.objects.filter(id=product_id)
    product.delete()
    return redirect(Product_list)
def product_edit(request,product_id):
    if request.method =="POST":
        product_name=request.POST.get('pname')
        product_rate=request.POST.get('prate')
        product_stoke=request.POST.get('pstock')
        product_details=request.POST.get('pdetail')
        product_cateogory=request.POST.get('productcat')
        Product.objects.filter(id=product_id).update(product_name=product_name,
                                        product_category=product_cateogory,
                                        product_rate=product_rate,
                                        product_details=product_details,
                                        product_stoke=product_stoke)
    
        return redirect(Product_list)
