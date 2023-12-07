from django.urls import path
from .views import room_list, room_detail
from bookings.views import book_room

urlpatterns = [
    path('', room_list, name='room_list'),
    path('<int:room_id>/', room_detail, name='room_detail'),
    path('<int:room_id>/book-application/', book_room, name='book_room'),
]
