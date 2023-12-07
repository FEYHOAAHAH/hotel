from django.shortcuts import render, redirect
from .models import Booking, Client
from rooms.models import Room


def book_room(request, room_slug):
    room = Room.objects.get(id=room_slug)

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        additional_services = request.POST.get('additional_services')

        if not full_name:

            return render(request, 'bookings/book_room.html', {'room': room, 'error_message': 'Full Name is required.'})

        client = Client.objects.create(full_name=full_name, email=email)
        booking = Booking.objects.create(
            client=client,
            room=room,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            additional_services=additional_services
        )

        return redirect('room_list')

    return render(request, 'bookings/book_room.html', {'room': room})
