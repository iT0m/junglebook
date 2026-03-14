from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
# Create your views here.

def product_list(request, category_slug=None):
    messages.success(request, "Welcome jungle shop")
    products=Product.objects.all()
    return render(request, 'shop/product/list.html', {'products':products})

def product_detail(request, id):
    product=get_object_or_404(Product, id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product':product, 'cart_product_form': cart_product_form})