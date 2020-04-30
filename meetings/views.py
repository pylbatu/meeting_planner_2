from django.shortcuts import render

from .models import Room, Meeting

# Create your views here.


def meetings(request):
    meetings = Meeting.objects.all()
    rooms = Room.objects.all()
    return render(request, 'meetings/meetings.html', {
        'meetings': meetings,
        'rooms': rooms
    })


def meeting(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, 'meetings/meeting.html', {
        'meeting': meeting
    })

