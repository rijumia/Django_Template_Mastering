from django.shortcuts import render
from productApp.models import*

def homePage(request):
    customerData = customerModel.objects.all()
    context = {
        'data': customerData
    }

    return render(request, 'home.html', context)

def productPage(request):
    productData = productModel.objects.all()
    context = {
        'data': productData
    }
    return render(request, 'products.html', context)

def addProduct(request):
    return render(request, 'addProduct.html')