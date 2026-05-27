# app_books/views.py
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Book


def book_list(request: HttpRequest) -> HttpResponse:
    """Render a page with a list of all books."""
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """Render a detail page for a single book by primary key."""
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})


def book_add(request: HttpRequest) -> HttpResponse:
    """Handle GET (show form) and POST (save book) for adding a new book."""
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        author = request.POST.get('author', '').strip()
        genre = request.POST.get('genre', '').strip()
        year = request.POST.get('year', '').strip()
        description = request.POST.get('description', '').strip()

        if not all([title, author, genre, year]):
            return render(request, 'book_add.html', {
                'error': 'Please fill in all required fields.'
            })

        Book.objects.create(
            title=title,
            author=author,
            genre=genre,
            year=int(year),
            description=description,
        )
        return HttpResponseRedirect(reverse('books:book_list'))

    return render(request, 'book_add.html')
