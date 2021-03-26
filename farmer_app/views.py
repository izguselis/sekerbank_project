from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib import messages

from .extras import generate_order_id
from .forms import *
from .tables import *


# Create your views here.
# def login(request):
#     if request.method == "POST":
#         # if 'submit' in request.POST:
#         #     return None
#         username = request.POST['username_id']
#         password = request.POST['password_id']
#         user = User.objects.filter(username=username, password=password)
#         if user.exists():
#             context = {
#                 "class": "nav-md",
#                 "user": user[0]
#             }
#             return render(request, "farmer_app/pages/index.html", context)
#         else:
#             messages.warning(request,
#                              'Kullanıcı bilgileri yanlış girilmiştir')
#     context = {
#         "class": "login"
#     }
#     return render(request, 'farmer_app/pages/login.html', context)


# def register(request):
#     if request.method == "POST":
#         form = UserForm(request.POST or None)
#         if form.is_valid():
#             # user = form.save()
#             # auth_login(request, user)
#             form.save()
#             return redirect("login")
#     else:
#         form = UserForm()
#     context = {
#         "class": "login",
#         "form": form
#     }
#     return render(request, "farmer_app/pages/register.html", context)


def reset_password(request):
    # message = ""
    if request.method == "POST":
        email = request.POST['email_id']
        new_password = request.POST['new_password_id']
        new_password_again = request.POST['new_password_again_id']
        if new_password_again != new_password:
            messages.warning(request, 'Şifreler aynı olmalıdır')
            # message = "Şifreler aynı olmalıdır"
        else:
            user = User.objects.get(email=email)
            if user:
                user.password = new_password
                user.save()
                return redirect("login")
            else:
                messages.warning(request,
                                 'Mail adresli kullanıcı bulunamamıştır')
            #  message = "Mail adresli kullanıcı bulunamamıştır"
    context = {
        "class": "login",
        # "messages": message
    }
    return render(request, "farmer_app/pages/reset_password.html", context)


def profile(request, user_id):
    user_profile = User.objects.filter(pk=user_id)
    orders = Order.objects.filter(is_ordered=True, owner=user_profile)
    context = {
        "class": "nav-md",
        "orders": orders
    }
    return render(request, "farmer_app/pages/profile.html", context)


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
            return redirect("category")
    context = {
        "class": "nav-md",
        "form": form
    }
    return render(request, 'farmer_app/pages/add_category.html', context)


def delete_category(request, category_id):
    deleted_category = Category.objects.get(pk=category_id)
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
            return redirect("product")

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
    item_count = get_item_count()
    sub_total = get_cart_total()
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
    # user_order, status = Order.objects.get_or_create(is_ordered=False)
    # user_order.items.add(order_item)
    # if status:
    #     user_order.ref_code = generate_order_id()
    #     user_order.save()
    # show confirmation message and redirect back to the same page
    messages.info(request, "Ürün sepete eklendi")
    return redirect("product")


def delete_from_cart(request, product_id):
    deleted_item = OrderItem.objects.get(pk=product_id)
    deleted_item.delete()
    messages.info(request, "Ürün sepetten silindi")
    return redirect("cart")


def purchase_cart(request, user_id):
    # get the user profile
    user_profile = User.objects.get(pk=user_id)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile,
                                                     is_ordered=False)
    items = OrderItem.objects.all()
    for item in items:
        user_order.items.add(item)
    if status:
        user_order.ref_code = generate_order_id()
        user_order.save()
        items.delete()
    messages.success(request, "Siparişiniz tamamlandı")
    return redirect("index")


def get_item_count():
    items = OrderItem.objects.all()
    return sum([item.quantity for item in items.all()])


def get_cart_total():
    items = OrderItem.objects.all()
    return sum([item.product.price for item in items.all()])
