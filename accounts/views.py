from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


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


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("farmer:index")
    else:
        form = AuthenticationForm()
    context = {
        "class": "login",
        "form": form
    }
    return render(request, "accounts/login.html", context)


def logout_view(request):
    # logout(request)
    return redirect("accounts:login")


def reset_password(request):
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
    context = {
        "class": "login"
    }
    return render(request, "farmer_app/pages/reset_password.html", context)
