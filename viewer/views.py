from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, FormView
from .models import Movie
from .forms import MovieForm
from logging import getLogger

LOGGER = getLogger()


class MoviesView(ListView):
    template_name = "viewer/movies.html"
    model = Movie


class MovieCreate(FormView):
    template_name = "form.html"
    form_class = MovieForm
    success_url = reverse_lazy("movie_create")

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Movie.objects.create(
            title=cleaned_data["title"],
            genre=cleaned_data["genre"],
            rating=cleaned_data["rating"],
            released=cleaned_data["released"],
            description=cleaned_data["description"]
        )
        return result

    def form_invalid(self, form):
        LOGGER.warning("User provided invalid data")
        return super().form_invalid(form)