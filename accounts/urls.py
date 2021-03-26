from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.conf import settings

app_name = "accounts"

urlpatterns = [
    # path('', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
]
