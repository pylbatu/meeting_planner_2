from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Room, Meeting
from .forms import MeetingForm

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

def new(request):
    if (request.method == 'POST'):
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MeetingForm()
    return render(request, 'meetings/new.html', {
        'form': form
    })

