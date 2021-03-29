from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # path('', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('reset_password/', views.reset_password, name="reset_password"),
    path('logout/', views.logout_view, name="logout"),
    # path('profile/', views.profile, name="profile"),
]
