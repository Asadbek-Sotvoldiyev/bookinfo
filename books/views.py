from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View

from books.forms import CommentForm
from books.models import Category, Book, Comment,SiteDesign,Genre


class CategoryView(View):
    def get(self,request,category_id):
        category = Category.objects.get(id=category_id)
        books = category.books.all()

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
            regular_ratings[book.id] = 5 - avg_rating

        data = {
            "books": books,
            "category":category,
            "ratings":ratings,
            "regular_ratings":regular_ratings,
        }
        return render(request, 'books/category.html', context=data)

class BookDetail(View):

    def get(self,request,pk):
        comments = Comment.objects.filter(book_id=pk)
        books = Book.objects.all()
        book = Book.objects.get(id=pk)
        form = CommentForm()

        comment_regular_ratings = {}
        for comment in comments:
            comment_regular_ratings[comment.id] = 5-comment.given_stars

        ratings = {}
        regular_ratings = {}
        for b in books:
            rating = 0
            for book_comment in book.comments.all():
                rating += book_comment.given_stars
            try:
                avg_rating = round(rating / len(book.comments.all()))
            except ZeroDivisionError:
                avg_rating = 0
            ratings[b.id] = avg_rating
            regular_ratings[b.id] = 5 - avg_rating

        data = {
            'book': book,
            'form_comment': form,
            'comments': comments,
            'ratings': ratings,
            'regular_ratings':regular_ratings,
            'regular_book_rate': comment_regular_ratings
        }
        return render(request, 'books/detail.html', context=data)

class AddCommentView(LoginRequiredMixin,View):
    def post(self,request,pk):
        form = CommentForm(request.POST)
        book = Book.objects.get(id=pk)
        if form.is_valid():
            Comment.objects.create(
                user = request.user,
                book = book,
                comment = form.cleaned_data['comment'],
                given_stars = form.cleaned_data['given_stars']
            )
            return redirect(reverse('books:detail', kwargs={'pk': book.id}))
        return render(request, 'books/detail.html', {'book':book,'form_comment':form})

def about(request):
    site = SiteDesign.objects.first()
    return render(request, 'books/about.html', context={'site':site})

def books(request):
    books = Book.objects.all()

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
        regular_ratings[book.id] = 5 - avg_rating

    data = {
        "books": books,
        "ratings": ratings,
        "regular_ratings": regular_ratings,
    }
    return render(request, 'books/books.html', context=data)

class GenresView(View):
    def get(self,request,genre_id):
        genre = Genre.objects.get(id=genre_id)
        books = genre.books.all()

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
            regular_ratings[book.id] = 5 - avg_rating

        data = {
            "books": books,
            "genre":genre,
            "ratings":ratings,
            "regular_ratings":regular_ratings,
        }
        return render(request, 'books/genres.html', context=data)


