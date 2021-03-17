from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from .forms import *
from .models import Category


# Create your views here.
def login(request):
    class_name = "login"
    return render(request, "farmer_app/pages/login.html",
                  {"class": class_name})


def register(request):
    class_name = "login"
    return render(request, "farmer_app/pages/register.html",
                  {"class": class_name})


def reset_password(request):
    class_name = "login"
    return render(request, "farmer_app/pages/reset_password.html",
                  {"class": class_name})


def index(request):
    class_name = "nav-md"
    return render(request, "farmer_app/pages/index.html",
                  {"class": class_name})


def category(request):
    class_name = "nav-md"
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            category_list = Category.objects.all()
            return render(request, "farmer_app/pages/category.html",
                          {"class": class_name,
                           "category_list": category_list})
    else:
        category_list = Category.objects.all()
        return render(request, "farmer_app/pages/category.html",
                      {"class": class_name, "category_list": category_list})


def product(request):
    class_name = "nav-md"
    if request.method == "POST":
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
        product_list = Product.objects.all()
        return render(request, "farmer_app/pages/product.html",
                      {"class": class_name, "product_list": product_list})

    else:
        product_list = Product.objects.all()
        return render(request, "farmer_app/pages/product.html",
                      {"class": class_name, "product_list": product_list})


def add_category(request):
    class_name = "nav-md"
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            category_list = Category.objects.all()
            return render(request, "farmer_app/pages/add_category.html",
                          {"class": class_name,
                           "category_list": category_list})
    else:
        category_list = Category.objects.all()
        return render(request, "farmer_app/pages/add_category.html",
                      {"class": class_name,
                       "category_list": category_list})


def delete_category(request, Category_id):
    deleted_category = Category.objects.get(pk=Category_id)
    deleted_category.delete()
    return redirect("category")


def update_category(request, Category_id):
    class_name = "nav-md"
    if request.method == "POST":
        updated_category = Category.objects.get(pk=Category_id)
        form = ListForm(request.POST or None, instance=updated_category)
        if form.is_valid():
            form.save()
            return redirect("category")
    else:
        category_list = Category.objects.all()
        return render(request, "farmer_app/pages/update_category.html",
                      {"category_list": category_list, "class": class_name})


def cart(request):
    class_name = "nav-md"
    return render(request, "farmer_app/pages/cart.html", {"class": class_name})


def add_cart(request, item_id):
    # filter products by id
    product = Product.objects.filter(
        id=item_id.get('item_id', "")).first()

    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect("product")
