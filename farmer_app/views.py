from django.shortcuts import render

# Create your views here.
from farmer_app.models import Category


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
    category_list = Category.objects.all()
    return render(request, "farmer_app/pages/category.html",
                  {"class": class_name, "category_list": category_list})


def product(request):
    class_name = "nav-md"
    return render(request, "farmer_app/pages/product.html",
                  {"class": class_name})


def add_category(request):
    class_name = "nav-md"
    return render(request, "farmer_app/pages/add_category.html",
                  {"class": class_name})
