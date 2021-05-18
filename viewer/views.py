from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Movie
from .forms import MovieForm
from logging import getLogger

LOGGER = getLogger()


class EditorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        editors_group = Group.objects.get(name="Editors")
        user_groups = self.request.user.groups.all()
        if editors_group in user_groups:
            return True
        else:
            return False
        # return editors_group in user_groups


class MoviesView(ListView):
    template_name = "viewer/movies.html"
    model = Movie


class MovieCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = MovieForm
    success_url = reverse_lazy("movie_create")
    permission_required = "viewer.add_movie"

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, "Movie added successfully")
        return result


    def form_invalid(self, form):
        messages.warning(self.request, "Invalid form")
        LOGGER.warning("User provided invalid data")
        return super().form_invalid(form)


class MovieUpdateView(EditorRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = "form.html"
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy("index")
    permission_required = "viewer.change_movie"

    def form_invalid(self, form):
        messages.warning(self.request, "Invalid form")
        LOGGER.warning("User provided invalid data during update of the movie")
        return super().form_invalid(form)


class MovieDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = "viewer/movie_confirm_delete.html"
    model = Movie
    success_url = reverse_lazy("index")
    permission_required = "viewer.delete_movie"


class MovieDetailView(DetailView):
    template_name = "viewer/movie_details.html"
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_groups'] = self.request.user.groups.all()
        context['user_permissions'] = self.request.user.get_all_permissions()
        return context