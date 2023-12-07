from django.urls import path

from django.urls import path
from .views import book_room

urlpatterns = [
    path('rooms/<slug:room_slug>/book-application/', book_room, name='book_room'),
]