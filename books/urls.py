from django.urls import path
from .views import CategoryView, BookDetail,AddCommentView,about,books,GenresView

app_name = 'books'
urlpatterns = [
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
    path('genre/<int:genre_id>/', GenresView.as_view(), name='genres'),
    path('detail/<int:pk>/', BookDetail.as_view(), name='detail'),
    path('add-comment/<int:pk>/', AddCommentView.as_view(), name='add_comment'),
    path('about/', about, name='about'),
    path('books/', books, name='books'),
]