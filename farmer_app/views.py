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
    item_count = get_item_count()
    context = {
        "class": "nav-md",
        "item_count": item_count
    }
    return render(request, "farmer_app/pages/index.html", context)


def category(request):
    category_table = CategoryTable(Category.objects.all())
    item_count = get_item_count()
    context = {
        "class": "nav-md",
        "table": category_table,
        "item_count": item_count
    }
    return render(request, "farmer_app/pages/category.html", context)


def add_category(request, category_id):
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


def product(request):
    product_table = ProductTable(Product.objects.all())
    item_count = get_item_count()
    context = {
        "class": "nav-md",
        "table": product_table,
        "item_count": item_count
    }
    return render(request, "farmer_app/pages/product.html", context)


def add_product(request, pk):
    if pk != '0':
        edit = Product.objects.get(pk=pk)
        form = ProductForm(instance=edit)
    else:
        form = ProductForm(request.POST, request.FILES)

    if request.method == 'POST':
        if pk != '0':
            form = ProductForm(request.POST, request.FILES, instance=edit)
        else:
            form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/add_product/' + pk)

    context = {
        "class": "nav-md",
        "form": form,
        "pk": pk
    }
    return render(request, 'farmer_app/pages/add_product.html', context)


def delete_product(request, product_id):
    deleted_product = Product.objects.get(pk=product_id)
    deleted_product.delete()
    return redirect("product")


def cart(request):
    items = OrderItem.objects.all()
    item_table = OrderItemTable(items)
    order = Order.objects.filter(is_ordered=False)
    item_count = get_item_count()
    sub_total = 0
    if order.exists():
        sub_total = order[0].get_cart_total()

    context = {
        "class": "nav-md",
        "table": item_table,
        "sub_total": sub_total,
        "item_list": items,
        "item_count": item_count
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


def delete_from_cart(request, product_id):
    deleted_item = OrderItem.objects.get(pk=product_id)
    deleted_item.delete()
    messages.info(request, "Ürün sepetten silindi")
    return redirect("cart")


def get_item_count():
    order = Order.objects.filter(is_ordered=False)
    if order.exists():
        item_count = order[0].get_cart_items()
        return item_count
    else:
        return 0
