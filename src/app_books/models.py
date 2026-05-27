# app_books/models.py
from django.db import models


class Book(models.Model):
    """Model representing a book in the library."""

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} ({self.author})"

    class Meta:
        ordering = ['-year']
