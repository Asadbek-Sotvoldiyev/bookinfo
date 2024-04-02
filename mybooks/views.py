from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from books.models import Book, Category, Genre
from users.forms import LoginForm,RegisterForm
from django.core.paginator import Paginator


def index(request):
    books = Book.objects.all()
    p = Paginator(books, 2)
    page = request.GET.get('page')
    book_page = p.get_page(page)
    page_nums = range(1,p.num_pages+1)


    categories = Category.objects.all()
    genres = Genre.objects.all()

    ratings = {}
    regular_ratings = {}
    for book in books:
        rating = 0
        for book_comment in book.comments.all():
            rating += book_comment.given_stars
        try:
            avg_rating = round(rating / len(book.comments.all()))
        except ZeroDivisionError:
            avg_rating = 0
        ratings[book.id] = avg_rating
        regular_ratings[book.id] = 5-avg_rating


    if request.method == 'POST':
        form = LoginForm(request.POST)
        forms = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('index'))
        if forms.is_valid():
            user = forms.save(commit=False)
            user.set_password(forms.cleaned_data['password'])
            user.save()
            return redirect(reverse('index'))
    else:
        form = LoginForm()
        forms = RegisterForm

    data = {
        "books": books,
        "categories":categories,
        "genres":genres,
        'form':form,
        'forms':forms,
        'ratings':ratings,
        'regular_ratings':regular_ratings,
        'book_page':book_page,
        'page_nums':page_nums
    }
    return render(request, 'mybooks.html', context=data)


