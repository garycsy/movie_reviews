from django.shortcuts import render

def home(request):
    searchMovie = request.GET.get("searchMovie")

    return render(request, "home.html", {"searchTerm": searchMovie})


def signup(request):
    email = request.GET.get("email")

    return render(request, "signup.html", {"email": email})