from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.conf import settings

app_name = "farmer"

urlpatterns = [
                  path('', views.index, name="index"),
                  # path('reset_password/', views.reset_password,
                  #      name="reset_password"),
                  path('profile/', views.profile, name="profile"),
                  path('category/', views.category, name="category"),
                  path('add_category/<category_id>', views.add_category,
                       name="add_category"),
                  path('delete_category/<category_id>', views.delete_category,
                       name="delete_category"),

                  path('product/', views.product, name="product"),
                  path('add_product/<pk>', views.add_product,
                       name="add_product"),
                  path('delete_product/<product_id>', views.delete_product,
                       name="delete_product"),

                  path('cart/', views.cart, name="cart"),
                  path('add_cart/<product_id>', views.add_cart,
                       name="add_cart"),
                  path('delete_from_cart/<product_id>', views.delete_from_cart,
                       name="delete_from_cart"),
                  path('purchase_cart/', views.purchase_cart,
                       name="purchase_cart"),

                  path('question/', views.question, name="question"),
                  path('add_question/', views.add_question,
                       name="add_question"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
