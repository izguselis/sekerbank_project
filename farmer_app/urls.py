from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('index/', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('reset_password/', views.reset_password, name="reset_password"),

    path('category/', views.category, name="category"),
    path('product/', views.product, name="product"),
    path('add_category/<category_id>', views.add_category, name="add_category"),
    path('delete_category/<Category_id>', views.delete_category,
         name="delete_category"),
    # path('update_category/<Category_id>', views.update_category,
    #      name="update_category"),

    path('add_product/<product_id>', views.add_product, name="add_product"),
    # path('update_product/<product_id>', views.update_product,
    #      name="update_product"),
    path('delete_product/<product_id>', views.delete_product,
         name="delete_product"),

    path('add_cart/<product_id>', views.add_cart, name="add_cart"),
    path('cart/', views.cart, name="cart"),
]
