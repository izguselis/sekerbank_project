from django.shortcuts import render, redirect

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
    return render(request, "farmer_app/pages/product.html",
                  {"class": class_name})


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


def add_cart(request, Category_id):
    class_name = "nav-md"
    if request.method == "POST":
        updated_category = Category.objects.get(pk=Category_id)
        form = ListForm(request.POST or None, instance=updated_category)
        if form.is_valid():
            form.save()
            return redirect("category")
    else:
        cart_list = Category.objects.all()
        return render(request, "farmer_app/pages/add_cart.html",
                      {"cart_list": cart_list, "class": class_name})
