from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('users/', include('users.urls')),
    path('', index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
