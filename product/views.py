from django.shortcuts import render,HttpResponse

# Create your views here.
def home (request):
    return render(request,'product/home.html')


def product (request):
    return render(request,'product/product.html')


def accessories (request):
    return render(request,'product/accessories.html')


def fashion (request):
    return render(request,'product/fashion.html')


def electronic (request):
    return render(request,'product/electronic.html')


def cart (request):
    return render(request,'product/cart.html')