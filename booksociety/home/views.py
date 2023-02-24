from django.shortcuts import render
from .models import Category,Products

def index(request):
    data=Category.objects.all()
    return render(request,"index.html",{"pro":data})

def category(request):
    id=request.GET["id"]
    cat=Category.objects.get(id=id)
    data=Products.objects.filter(pro_id=id)
    return render(request,"category.html",{"category":data})


def details(request):
    id=request.GET["id"]
    data=Products.objects.filter(id=id)
    return render(request,"details.html",{"pro":data})

    
def pay(request):
    if request.method=="POST":
        id=request.GET["id"]
        quantity=request.POST["quantity"]
        print(quantity)
        data=Products.objects.filter(id=id)
    return render(request,"payment.html",{"pro":data,"quantity":quantity})


def about(request):
    return render(request,"about.html")

