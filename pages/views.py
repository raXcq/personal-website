from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def home_page_view(request):
    return HttpResponse("My Personal Website")


def about_page_view(request):
    context = {
        "name": "John Doe",
        "age": 24,
    }

    return render(request, "pages/about.html", context)
