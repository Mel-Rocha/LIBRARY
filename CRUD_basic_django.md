# CRUD Basic

<aside>
💡 Tutorial de como criar um CRUD básico no django.

</aside>

**************Índice**************

# Pré-Requisitos

Python e django baixados e instalados na máquina.

# Parte 1 - Configuração Geral e Estrutura

1 - Crie uma pasta no cmd, navegue até a pasta e crie as subpastas templates e static

```python
mkdir folder # pasta onde ficará tudo, docs, scr, tests etc
cd folder
mkdir templates #arquivo de base html ficará aqui
mkdir static #imagens e js 
```

2 - Crie um ambiente virtual e ative-o

```python
python3 -m venv env
env\Scripts\activate
```

3 - Instale o django no ambiente virtual

```python
pip install django
```

4 - Crie o projeto django dentro da pasta folder

```python
django-admin startproject core .
```

5 - Crie um aplicativo django 

```python
python [manage.py](http://manage.py/) startapp my_app
```

6 - Instale o app, no path folder/core/settings.py

```python
# Adicione 'my_app' à lista de 
'INSTALLED_APPS’INSTALLED_APPS = [
...
'my_app',
]
```

7 - Faça as migrações das tabelas para o banco

```python
python [manage.py](http://manage.py/) migrate
```

8 - Crie o superuser (informe email e senha, e os use como login para admin posteriormente)

```python
python [manage.py](http://manage.py/) createsuperuser
```

9 - Rode o servidor, após executar o comando abaixo acesse [http://localhost:8000](http://localhost:8000/)

```python
python [manage.py](http://manage.py/) runserver
```

10 - Faça login como admin, acesse [http://localhost:8000/admin](http://localhost:8000/admin)

# Parte 2 - Crie as Models

1 - No aplicativo, navegue até o caminho: my_app/models.py, e crie as classes do modelo 

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100) 
    publication_date = models.DateField()

    def __str__(self):
        return self.title
```

2 - Faça as migrações para criar as tabelas no banco de dados.

```python
python [manage.py](http://manage.py/) makemigrations
python [manage.py](http://manage.py/) migrate
```

3 - Habilite os modelos para a área administrativa. Vá até my_app/admin.py, crie a classe BookAdmin e defina os campos da model no list_display para poder visualizá-los na área administrativa.

```python
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')

admin.site.register(Book, BookAdmin)
```

# Parte 3 - Crie os Forms

1 - No aplicativo crie o arquivo para formulários my_app/forms.py

2 - No arquivo [forms.py](http://forms.py/), importe o módulo forms do Django e a classe Book do arquivo [models.py](http://models.py/). Em seguida, crie a classe BookForm que herda da classe forms.ModelForm:

```python
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date')
```

# Parte 4 - Crie as Views

1- No aplicativo, abra my_app/views.py, importe a model Book e o BookForm do forms, além dos demais imports de django.shortcuts e defina a lógica da aplicação em cada view.

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_create.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('my_app:book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_update.html', {'form': form, 'book': book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('my_app:book_list')
    return render(request, 'books/book_delete.html', {'book': book})
```

# Parte 5 - Configure as URLs

1 - No aplicativo crie o arquivo [urls.py](http://urls.py/), dessa forma, my_app/urls.py

2 - Em my_app/urls.py, importe os módulos necessários, e defina as URLs específicas para cada view:

```python
from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/update/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
]
```

3 - No projeto, vá para o arquivo [urls.py](http://urls.py/) (core/urls.py), importe o include e as urls do aplicativo.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),
]
```

# Parte 6 - Crie os Templates

1 - Vá até a pasta templates na raiz do projeto, e crie o arquivo base.html, assim templates/base.html, e digite o código:

```html
<!DOCTYPE html>
<html>
<head>
<title>Meu Aplicativo</title>
</head>
<body>
<header>
<!-- Seu cabeçalho -->
</header>
<main>
    {% block content %}<!--o conteúdo de cada página extendida...-->
    {% endblock %}<!--...aparecerá entre essa tag-->
</main>

<footer>
    <!-- Seu rodapé -->
</footer>
</body>
</html>

```

2 - No projeto, altere as configurações vá até core/settings.py e importe os

```python
from pathlib import Path
import os
```

3 - ainda em core/settings.py defina:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],#adicione aqui
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

4 - No aplicativo, crie a pasta templates e a subpasta books, assim my_app/templates/books

5 - No path my_app/templates/books crie os arquivos book_create.html, book_delete.html, book_list.html e book_update.html

6 - Em my_app/templates/books/book_list.html

```html
{% extends 'base.html' %}

{% block title %}Book List{% endblock %}

{% block content %}
<h1>Book List</h1>
<table>
    <thead>
        <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Publication Date</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for book in books %}
        <tr>
            <td>{{ book.title }}</td>
            <td>{{ book.author }}</td>
            <td>{{ book.publication_date }}</td>
            <td>
                <a href="{% url 'my_app:book_update' book.pk %}">Edit</a>
                <a href="{% url 'my_app:book_delete' book.pk %}">Delete</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
<a href="{% url 'my_app:book_create' %}">Add Book</a>
{% endblock %}
```

7 - Em my_app/templates/books/book_create.html

```html
{% extends 'base.html' %}

{% block title %}Create Book{% endblock %}

{% block content %}
<h1>Create Book</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
</form>
{% endblock %}
```

8 - Em my_app/templates/books/book_update.html

```html
{% extends 'base.html' %}

{% block title %}Update Book{% endblock %}

{% block content %}
<h1>Update Book</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Update</button>
</form>
{% endblock %}
```

9 - Em my_app/templates/books/book_delete.html

```html
{% extends 'base.html' %}

{% block title %}Delete Book{% endblock %}

{% block content %}
<h1>Delete Book</h1>
<p>Are you sure you want to delete "{{ book.title }}"?</p>
<form method="post">
    {% csrf_token %}
    <button type="submit">Delete</button>
</form>
{% endblock %}
```