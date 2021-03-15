from django.shortcuts import render


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
    return render(request, "farmer_app/pages/category.html",
                  {"class": class_name})
