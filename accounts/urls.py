from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


app_name = "accounts"
urlpatterns = [
    path("login/", views.SubmittableLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password-change/", views.SubmittablePasswordChange.as_view(), name="password_change"),
    path("sign-up/", views.SignUpView.as_view(), name="sign_up"),
]