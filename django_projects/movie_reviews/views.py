from django.shortcuts import render
from .models import Movie


def home(request):
    searchMovie = request.GET.get("searchMovie")
    movies = Movie.objects.all()

    return render(request, "home.html", {"searchTerm": searchMovie, 'movies': movies})

def signup(request):
    email = request.GET.get("email")

    return render(request, "signup.html", {"email": email})


