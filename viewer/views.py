from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import Movie

# Create your views here.
def hello(request):
    s_parameter = request.GET.get("s", '')
    return render(request, template_name="viewer/hello_simple.html", context={'s': s_parameter})


def hello_with_parameter(request, s):
    s1 = request.GET.get("s1", '')
    return render(
        request,
        template_name="viewer/hello.html",
        context={"adjectives": [s, s1, "Wonderful", "Man's"]}
    )


class GenericMoviesView(View):
    def get(self, request):
        return render(
            request,
            template_name="viewer/movies.html",
            context={"movies": Movie.objects.all()}
        )


class TemplateMoviesView(TemplateView):
    template_name = "viewer/movies.html"
    extra_context = {"movies": Movie.objects.all()}


class MoviesView(ListView):
    template_name = "viewer/movies.html"
    model = Movie