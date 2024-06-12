from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, Author


def film_list(request):
    films = Film.objects.all()
    return render(request, 'film_list.html', {'films': films})


def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'film_detail.html', {'film': film})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'author_detail.html', {'author': author})


def film_stats(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'film_stats.html', {'film': film})


def film_edit(request, pk):
    film = get_object_or_404(Film, pk=pk)
    if request.method == "POST":
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            film = form.save(commit=False)
            film.save()
            return redirect('film_detail', pk=film.pk)
    else:
        form = FilmForm(instance=film)
    return render(request, 'film_edit.html', {'form': form})
