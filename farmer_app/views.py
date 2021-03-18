from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import *
from .models import *
from .tables import *


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
    category_table = Category.objects.all()
    table = CategoryTable(category_table)
    context = {
        "class": "nav-md",
        "table": table
    }
    return render(request, "farmer_app/pages/category.html", context)


def add_category(request, category_id):
    class_name = "nav-md"
    if category_id != '0':
        edit = Category.objects.get(pk=category_id)
        form = CategoryForm(instance=edit)
    else:
        form = CategoryForm(request.POST, request.FILES)
    if request.method == "POST":
        if category_id != '0':
            form = CategoryForm(request.POST, request.FILES, instance=edit)
        else:
            form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {
        "class": "nav-md",
        "form": form
    }
    return render(request, 'farmer_app/pages/add_category.html', context)


def delete_category(request, Category_id):
    deleted_category = Category.objects.get(pk=Category_id)
    deleted_category.delete()
    return redirect("category")


# def update_category(request, Category_id):
#     class_name = "nav-md"
#     if request.method == "POST":
#         updated_category = Category.objects.get(pk=Category_id)
#         form = CategoryForm(request.POST or None, instance=updated_category)
#         if form.is_valid():
#             form.save()
#             return redirect("category")
#     else:
#         category_list = Category.objects.all()
#         return render(request, "farmer_app/pages/update_category.html",
#                       {"category_list": category_list, "class": class_name})


def product(request):
    class_name = "nav-md"
    product_table = Product.objects.all()
    table = ProductTable(product_table)
    context = {
        "class": "nav-md",
        "table": table
    }
    return render(request, "farmer_app/pages/product.html", context)


def add_product(request, product_id):
    if product_id != '0':
        edit = Product.objects.get(pk=product_id)
        form = ProductForm(instance=edit)
    else:
        form = ProductForm(request.POST, request.FILES)

    if request.method == 'POST':
        if product_id != '0':
            form = ProductForm(request.POST, request.FILES, instance=edit)
        else:
            form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {
        "class": "nav-md",
        "form": form
    }
    return render(request, 'farmer_app/pages/add_product.html', context)


# def update_product(request, product_id):
#     class_name = "nav-md"
#     edit = Product.objects.get(pk=product_id)
#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES, instance=edit)
#         if form.is_valid():
#             form.save()
#             return redirect("product")
#     else:
#         form = ProductForm(instance=edit)
#         return render(request, 'farmer_app/pages/update_product.html',
#                       {"class": class_name, "form": form})


def delete_product(request, product_id):
    deleted_product = Product.objects.get(pk=product_id)
    deleted_product.delete()
    return redirect("product")


def cart(request):
    items = OrderItem.objects.all()
    item_table = OrderItemTable(items)
    order = Order.objects.filter(is_ordered=False).first()
    sub_total = order.get_cart_total()
    context = {
        'class': "nav-md",
        'table': item_table,
        'sub_total': sub_total,
        'item_list': items
    }
    return render(request, "farmer_app/pages/cart.html", context)


def add_cart(request, product_id):
    # filter products by id
    product = Product.objects.get(pk=product_id)
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(is_ordered=False)
    user_order.items.add(order_item)
    if status:
        user_order.save()
    # show confirmation message and redirect back to the same page
    messages.info(request, "Ürün sepete eklendi")
    return redirect("product")
