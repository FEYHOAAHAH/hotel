from django.db import models
from rooms.models import Room


class Client(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()


class Booking(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    additional_services = models.TextField()
    is_approved = models.BooleanField(default=False)
