from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import SignUpForm


class SubmittableLoginView(LoginView):
    template_name = "form.html"


class SubmittablePasswordChange(PasswordChangeView):
    template_name = "form.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, "Password Changed successfully")
        return result


class SignUpView(CreateView):
    template_name = "form.html"
    form_class = SignUpForm
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, "User Created successfully")
        return result