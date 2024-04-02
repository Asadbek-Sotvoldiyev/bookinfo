from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]