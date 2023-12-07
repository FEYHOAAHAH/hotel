from django.shortcuts import render, redirect
from .models import Room


def room_list(request):
    rooms = Room.objects.filter(is_reserved=False)
    return render(request, 'rooms/room_list.html', {'rooms': rooms})


def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)
    return render(request, 'rooms/room_detail.html', {'room': room})
