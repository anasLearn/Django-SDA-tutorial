from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Movie
from .forms import MovieForm
from logging import getLogger

LOGGER = getLogger()



class MoviesView(ListView):
    template_name = "viewer/movies.html"
    model = Movie


class MovieCreateView(LoginRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = MovieForm
    success_url = reverse_lazy("movie_create")

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, "Movie added successfully")
        return result


    def form_invalid(self, form):
        messages.warning(self.request, "Invalid form")
        LOGGER.warning("User provided invalid data")
        return super().form_invalid(form)


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "form.html"
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy("index")

    def form_invalid(self, form):
        messages.warning(self.request, "Invalid form")
        LOGGER.warning("User provided invalid data during update of the movie")
        return super().form_invalid(form)


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "viewer/movie_confirm_delete.html"
    model = Movie
    success_url = reverse_lazy("index")


class MovieDetailView(DetailView):
    template_name = "viewer/movie_details.html"
    model = Movie