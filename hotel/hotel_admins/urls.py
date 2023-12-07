from django.urls import path
from .views import admin_home, add_room, admin_room_list, admin_book_applications, admin_booking_detail, \
    admin_booking_approval

urlpatterns = [
    path('', admin_home, name='admin_home'),
    path('add-room/', add_room, name='add_room'),
    path('rooms/', admin_room_list, name='admin_room_list'),
    path('book-applications/', admin_book_applications, name='admin_book_applications'),
    path('book-applications/<slug:booking_slug>/', admin_booking_detail, name='admin_booking_detail'),
    path('book-applications/<slug:booking_slug>/approval/', admin_booking_approval, name='admin_booking_approval'),
]
