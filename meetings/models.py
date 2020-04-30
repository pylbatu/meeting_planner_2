from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=32)
    floor = models.IntegerField()

    def __str__(self):
        return f'Room {self.name}'

class Meeting(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'Meeting {self.title} on {self.date}'