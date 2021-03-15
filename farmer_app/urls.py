from . import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('index/', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('reset_password/', views.reset_password, name="reset_password"),
    path('category/', views.category, name="category"),
    path('product/', views.product, name="product"),
    path('add_category/', views.add_category, name="add_category"),
]
