from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    s = request.GET.get("s", '')
    return HttpResponse(f"Hello {s} World")


def hello_with_parameter(request, s):
    return HttpResponse(f"Hello {s}!")