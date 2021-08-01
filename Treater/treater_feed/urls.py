from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("home", views.home, name="home"),
    path("add_tweet", views.add_tweet, name="add_tweet"),
    path("profile", views.view_own_profile, name="view_own_profile"),
    path("user_profile/<int:user_id>", views.view_user_profile, name="view_user_profile")
]