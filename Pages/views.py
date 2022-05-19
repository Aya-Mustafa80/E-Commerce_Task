from contextlib import _RedirectStream
from django.shortcuts import render
from django.http import HttpResponse
from .models import Categories,Products

# Create your views here.
def home(request): 
    Product=Products.objects.filter(orderd=True)
    count=Product.count
    PRoducts=Products.objects.all()[:4]
    return render(request,'index.html',{ 'Products':PRoducts,'count':count})


def shop(request):
    Product=Products.objects.filter(orderd=True)
    count=Product.count
    Cato=Categories.objects.all()
    PRoducts=Products.objects.all()
    return render(request,'product.html',{ 'Products':PRoducts,'Category':Cato,'count':count})


def shopre(request,catid):
    Product=Products.objects.filter(orderd=True)
    count=Product.count
    Cato=Categories.objects.all()
    PRoducts=Products.objects.all().filter(catego=catid)
    if catid==0:
        PRoducts=Products.objects.all()
    else:
        PRoducts = Products.objects.filter(catego=catid)
    return render(request,'product.html',{ 'Products':PRoducts,'Category':Cato,'count':count})

def prodDetail(request,prodid):
    Product=Products.objects.filter(orderd=True)
    count=Product.count
    Product=Products.objects.get(id=prodid)
    return render(request,'product-detail.html',{'Product':Product,'count':count})

def about(request):
    Product=Products.objects.filter(orderd=True)
    count=Product.count
    return render(request,'about.html',{'count':count})
 
def contact(request):
    Product=Products.objects.filter(orderd=True)
    count=Product.count
    return render(request,'contact.html',{'count':count})

def shopCart(request):
    Product=Products.objects.filter(orderd=True)
    count=Product.count
    return render(request,'shoping-cart.html',{'Products':Product,'count':count})
    
def cart(request,pID):
    Product=Products.objects.get(id=pID)
    Product.orderd=True
    Product.save()
    Pro=Products.objects.filter(orderd=True)
    count=Pro.count
    return render(request,'product-detail.html',{'Product':Product,'count':count})


def Cartdel(request,CID):
    Product=Products.objects.get(id=CID)
    Product.orderd=False
    Product.save()
    Pro=Products.objects.filter(orderd=True)
    count=Pro.count
    return render(request,'shoping-cart.html',{'Products':Pro,'count':count})

