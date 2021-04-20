from django.shortcuts import render
from django.http import HttpResponse
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

def movies(request):
    my_movies = Movie.objects.all()
    return render(
        request,
        template_name="viewer/movies.html",
        context={"movies": my_movies}
    )