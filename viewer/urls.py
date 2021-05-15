from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.MovieCreateView.as_view(), name="movie_create"),
    path('update/<pk>/', views.MovieUpdateView.as_view(), name="movie_update"),
    path('delete/<pk>/', views.MovieDeleteView.as_view(), name="movie_delete"),
    path("details/<pk>/", views.MovieDetailView.as_view(), name="movie_details"),
]