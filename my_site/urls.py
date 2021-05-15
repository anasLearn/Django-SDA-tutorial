from django.contrib import admin
from django.urls import path, include
from viewer.views import MoviesView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', MoviesView.as_view(), name="index"),
    path("movie/", include('viewer.urls')),
    path("accounts/", include('accounts.urls')),
]
