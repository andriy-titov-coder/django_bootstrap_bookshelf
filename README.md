# <span style="background: #3b2b4b;color:white;padding:4px 8px;border-radius:6px;">📚</span> BookShelf | Django + Bootstrap

![Django](https://img.shields.io/badge/Django-5.1-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

---

A **Django web application** for managing a personal book list.

Built with **Django 5** and styled with **Bootstrap 5** via **CDN** - no custom **CSS** required.

---

## <span style="background: #3b2b4b;color:white;padding:4px 8px;border-radius:6px;">🚀</span> Tech Stack

| Layer     | Technology              |
|-----------|-------------------------|
| Backend   | `Django 5.1`            |
| Database  | `SQLite` (built-in)     |
| Frontend  | `Bootstrap 5.3` via CDN |
| Templates | `Django Template Language (DTL)` |

---

## <span style="background: #3b2b4b;color:white;padding:4px 8px;border-radius:6px;">✅</span> Features

- **Book List**: View all books in a responsive **Bootstrap** table
- **Book Detail**: Detailed view of each book using **Bootstrap Card** + **Grid**
- **Book Add**: Add new books via a **Bootstrap**-styled form with validation
- **Responsive Design**: Mobile-friendly layout using **Bootstrap 5**
- **Seed Script**: Pre-populate the database with **15** classic books

---

## <span style="background: #3b2b4b;color:white;padding:4px 8px;border-radius:6px;">📂</span> Project Structure

```
django_bootstrap_bookshelf/
├── src/
│   ├── app_books/
│   │   ├── migrations/
│   │   ├── models.py        # Book ORM model
│   │   ├── urls.py          # App URL routes
│   │   └── views.py         # View functions
│   ├── config/
│   │   ├── settings.py      # Django settings
│   │   └── urls.py          # Root URL config
│   ├── templates/
│   │   ├── base.html        # Bootstrap CDN + navbar + blocks
│   │   ├── book_list.html   # Bootstrap Table + Badge
│   │   ├── book_detail.html # Bootstrap Card + Grid
│   │   └── book_add.html    # Bootstrap Form + Alert
│   ├── add_new_books.py     # Database seed script
│   └── manage.py
└── requirements.txt
```

---

## <span style="background: #3b2b4b;color:white;padding:4px 8px;border-radius:6px;">⚡</span> Quick Start

```bash
git clone git@github.com:YOUR_USERNAME/django_bootstrap_bookshelf.git
cd django_bootstrap_bookshelf

python -m venv venv
source venv/bin/activate      # Mac/Linux
# venv\Scripts\activate       # Windows

pip install -r requirements.txt

cd src
python manage.py migrate
python manage.py runserver
```

Open: **http://127.0.0.1:8000/books/**

### Seed the database (optional)

```bash
python add_new_books.py
```

---

## <span style="background: #3b2b4b;color:white;padding:4px 8px;border-radius:6px;">🌐</span> Pages

| URL                              | Description                     |
|----------------------------------|---------------------------------|
| `http://127.0.0.1:8000/books/`   | Book list with Bootstrap table  |
| `http://127.0.0.1:8000/books/add/` | Add new book form             |
| `http://127.0.0.1:8000/books/1/` | Book detail card                |

---

## <span style="background: #3b2b4b;color:white;padding:4px 8px;border-radius:6px;">🎨</span> Bootstrap Components Used

| Component       | Used In          | Purpose                          |
|-----------------|------------------|----------------------------------|
| `navbar`        | `base.html`      | Responsive top navigation        |
| `table`         | `book_list.html` | Displaying books with hover/stripe |
| `badge`         | `book_list.html` | Genre label                      |
| `alert`         | `book_add.html`  | Validation error message         |
| `card`          | `book_detail.html`, `book_add.html` | Content containers  |
| `form-control`  | `book_add.html`  | Styled input fields              |
| `btn`           | All pages        | Action buttons                   |
| `container`     | `base.html`      | Centered, responsive layout      |

---

## <span style="background: #3b2b4b;color:white;padding:4px 8px;border-radius:6px;">👤</span> Author

Built as a learning example for **Django + Bootstrap** integration.
