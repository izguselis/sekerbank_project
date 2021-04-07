from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import translation
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate

from .extras import generate_order_id
from .forms import *
from .tables import *


# Create your views here.

# def reset_password(request):
#     # message = ""
#     if request.method == "POST":
#         email = request.POST['email_id']
#         new_password = request.POST['new_password_id']
#         new_password_again = request.POST['new_password_again_id']
#         if new_password_again != new_password:
#             messages.warning(request, 'Şifreler aynı olmalıdır')
#             # message = "Şifreler aynı olmalıdır"
#         else:
#             user = User.objects.get(email=email)
#             if user:
#                 user.password = new_password
#                 user.save()
#                 return redirect("login")
#             else:
#                 messages.warning(request,
#                                  'Mail adresli kullanıcı bulunamamıştır')
#             #  message = "Mail adresli kullanıcı bulunamamıştır"
#     context = {
#         "class": "login",
#         # "messages": message
#     }
#     return render(request, "farmer_app/pages/reset_password.html", context)

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
    finally:
        activate(cur_language)


@login_required()
def profile(request):
    item_count = get_item_count()
    orders = Order.objects.filter(is_ordered=True, owner=request.user)
    context = {
        "class": "nav-md",
        "orders": orders,
        "item_count": item_count
    }
    return render(request, "farmer_app/pages/profile.html", context)


@login_required()
def index(request):
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]
    context = get_context()
    # book = Book(ISBN="1234567890")
    # book.save()
    # book_en = BookTranslation(language_code='en')
    # book_en.title = "Django for Dummies"
    # book_en.description = "Django described in simple words."
    # book_en.parent = book
    # book_en.save()
    # book_list = BookTranslation.objects.all()
    # context.update({"book_list": book_list})
    return render(request, "farmer_app/pages/index.html", context)


@login_required()
def category(request):
    category_table = CategoryTable(Category.objects.all())
    context = get_context()
    context.update({"table": category_table})
    return render(request, "farmer_app/pages/category.html", context)


@login_required()
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
            return redirect("farmer:category")
    context = get_context()
    context.update({"form": form})
    return render(request, 'farmer_app/pages/add_category.html', context)


@login_required()
def delete_category(request, category_id):
    deleted_category = Category.objects.get(pk=category_id)
    deleted_category.delete()
    return redirect("farmer:category")


@login_required()
def product(request):
    product_table = ProductTable(Product.objects.all())
    context = get_context()
    context.update({"table": product_table})
    return render(request, "farmer_app/pages/product.html", context)


@login_required()
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
            return redirect("farmer:product")
    context = get_context()
    context.update({"form": form})
    return render(request, 'farmer_app/pages/add_product.html', context)


@login_required()
def delete_product(request, product_id):
    deleted_product = Product.objects.get(pk=product_id)
    deleted_product.delete()
    return redirect("farmer:product")


@login_required()
def cart(request):
    items = OrderItem.objects.filter(is_ordered=False)
    item_table = OrderItemTable(items)
    sub_total = get_cart_total()
    context = get_context()
    context.update({"sub_total": sub_total,
                    "table": item_table})
    return render(request, "farmer_app/pages/cart.html", context)


@login_required()
def add_cart(request, product_id):
    # filter products by id
    added_product = Product.objects.filter(pk=product_id).first()
    # create orderItem of the selected product
    OrderItem.objects.get_or_create(product=added_product)
    # show confirmation message and redirect back to the same page
    messages.info(request, "Ürün sepete eklendi")
    return redirect("farmer:product")


@login_required()
def delete_from_cart(request, product_id):
    deleted_item = OrderItem.objects.get(pk=product_id)
    deleted_item.delete()
    messages.info(request, "Ürün sepetten silindi")
    return redirect("farmer:cart")


@login_required()
def purchase_cart(request):
    # get the user profile
    user_profile = request.user
    # create order associated with the user
    user_order = Order.objects.create(owner=user_profile,
                                      is_ordered=True)
    items = OrderItem.objects.filter(is_ordered=False)
    for item in items:
        item.is_ordered = True
        item.save()
        user_order.items.add(item)
    user_order.ref_code = generate_order_id()
    user_order.save()
    messages.success(request, "Siparişiniz tamamlandı")
    return redirect("farmer:index")


def book(request):
    cur_language = get_language()
    book_table = BookTable(
        BookTranslation.objects.filter(language_code=cur_language))
    context = get_context()
    context.update({"table": book_table})
    return render(request, "farmer_app/pages/book.html", context)


def get_item_count():
    items = OrderItem.objects.filter(is_ordered=False)
    return sum([item.quantity for item in items.all()])


def get_cart_total():
    items = OrderItem.objects.filter(is_ordered=False)
    return sum([item.product.price for item in items.all()])


def get_context():
    item_count = get_item_count()
    context = {
        "class": "nav-md",
        "item_count": item_count,
        "home_page": _("Giriş Ekranı"),
        "category_page": _("Kategoriler"),
        "product_page": _("Ürünler"),
        "book_page": _("Kitaplar"),
        "profile_page": _("Profilim"),
        "change_password": _("Şifre Değiştir"),
        "quit": _("Çıkış Yap"),
        "language": _("Dil"),
    }
    return context
