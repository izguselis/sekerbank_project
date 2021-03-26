from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = UserCreationForm()
    context = {
        "class": "login",
        "form": form
    }
    return render(request, "accounts/register.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect("farmer:index")
    else:
        form = AuthenticationForm()
    context = {
        "class": "login",
        "form": form
    }
    return render(request, "accounts/login.html", context)
