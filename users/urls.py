from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("login", views.login_view, name="login"),
    # path("login", auth_views.LoginView.as_view(template_name="auctions/login.html"), name="login"),
    # path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile")
]