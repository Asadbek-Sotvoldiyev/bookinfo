from django.contrib import admin
from .models import Book, Comment, Category, Genre,SiteDesign

admin.site.register([Comment, Category, Genre,Book,SiteDesign])
