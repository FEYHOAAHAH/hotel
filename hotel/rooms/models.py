from django.db import models
from django.urls import reverse


class Room(models.Model):
    ROOM_TYPES = [
        ('cheap', 'Дешёвые'),
        ('comfortable', 'Комфортные'),
        ('vip', 'V.I.P.'),
    ]

    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    is_reserved = models.BooleanField(default=False)
    details = models.TextField()

    def get_absolute_url(self):
        return reverse('room_detail', args=[str(self.id)])
