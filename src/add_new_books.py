# src/add_new_books.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from app_books.models import Book

books = [
    {
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'genre': 'Fiction',
        'year': 1960,
        'description': 'A story of racial injustice and moral growth in the American South.',
    },
    {
        'title': 'The Sound and the Fury',
        'author': 'William Faulkner',
        'genre': 'Fiction',
        'year': 1929,
        'description': "A Southern family's decline told through multiple perspectives and timelines.",
    },
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'genre': 'Magical Realism',
        'year': 1967,
        'description': 'Seven generations of the Buendia family in the mythical town of Macondo.',
    },
    {
        'title': '1984',
        'author': 'George Orwell',
        'genre': 'Dystopian',
        'year': 1949,
        'description': 'A chilling vision of a totalitarian future under constant surveillance.',
    },
    {
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'genre': 'Fiction',
        'year': 1925,
        'description': 'A critique of the American Dream set in the Jazz Age.',
    },
    {
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'genre': 'Romance',
        'year': 1813,
        'description': 'A classic story of love, class, and misunderstanding.',
    },
    {
        'title': 'The Catcher in the Rye',
        'author': 'J.D. Salinger',
        'genre': 'Fiction',
        'year': 1951,
        'description': 'A teenager journey through alienation and identity.',
    },
    {
        'title': 'The Hobbit',
        'author': 'J.R.R. Tolkien',
        'genre': 'Fantasy',
        'year': 1937,
        'description': 'A hobbit embarks on an unexpected adventure to reclaim a lost kingdom.',
    },
    {
        'title': 'The Lord of the Rings',
        'author': 'J.R.R. Tolkien',
        'genre': 'Fantasy',
        'year': 1954,
        'description': 'An epic quest to destroy a powerful ring and defeat evil.',
    },
    {
        'title': 'Harry Potter and the Sorcerers Stone',
        'author': 'J.K. Rowling',
        'genre': 'Fantasy',
        'year': 1997,
        'description': 'A young wizard begins his journey at Hogwarts.',
    },
    {
        'title': 'The Alchemist',
        'author': 'Paulo Coelho',
        'genre': 'Philosophical Fiction',
        'year': 1988,
        'description': 'A shepherd travels in search of his personal legend.',
    },
    {
        'title': 'The Little Prince',
        'author': 'Antoine de Saint-Exupery',
        'genre': 'Fable',
        'year': 1943,
        'description': 'A poetic tale about life, love, and human nature.',
    },
    {
        'title': 'Brave New World',
        'author': 'Aldous Huxley',
        'genre': 'Dystopian',
        'year': 1932,
        'description': 'A futuristic society driven by technology and control.',
    },
    {
        'title': 'Fahrenheit 451',
        'author': 'Ray Bradbury',
        'genre': 'Dystopian',
        'year': 1953,
        'description': 'A world where books are banned and burned.',
    },
    {
        'title': 'The Da Vinci Code',
        'author': 'Dan Brown',
        'genre': 'Thriller',
        'year': 2003,
        'description': 'A fast-paced mystery involving secret societies and hidden codes.',
    },
]

for data in books:
    book, created = Book.objects.get_or_create(title=data['title'], defaults=data)
    status = 'Created' if created else 'Already exists'
    print(f"{status}: {book.title}")

print('\nDone!')
