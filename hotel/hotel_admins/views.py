from django.shortcuts import render

# Create your views here.
# hotel_admins/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from bookings.models import Client, Booking
from rooms.models import Room


def admin_home(request):
    return render(request, 'hotel_admins/admin_home.html')


def add_room(request):
    if request.method == 'POST':
        room_type = request.POST.get('room_type')
        details = request.POST.get('details')
        Room.objects.create(room_type=room_type, details=details)
        return redirect('admin_room_list')
    return render(request, 'hotel_admins/add_room.html')


def admin_room_list(request):
    rooms = Room.objects.all()
    return render(request, 'hotel_admins/admin_room_list.html', {'rooms': rooms})


def admin_book_applications(request):
    bookings = Booking.objects.all()
    return render(request, 'hotel_admins/admin_book_applications.html', {'bookings': bookings})


def admin_booking_detail(request, booking_slug):
    booking = get_object_or_404(Booking, slug=booking_slug)
    return render(request, 'hotel_admins/admin_booking_detail.html', {'booking': booking})


def admin_booking_approval(request, booking_slug):
    booking = get_object_or_404(Booking, slug=booking_slug)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'approve':
            booking.is_approved = True
            booking.save()
        elif action == 'reject':
            booking.delete()

        return redirect('admin_book_applications')

    return HttpResponse("Invalid Request")
