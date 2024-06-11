from django.shortcuts import render
from .models import Film, Author

def home(request):
    films = Film.objects.all()
    return render(request, 'home.html', {'films': films})
def film_detail(request, film_id):
    film = Film.objects.get(id=film_id)
    return render(request, 'film_detail.html', {'film': film})

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'author_detail.html', {'author': author})

