from django.urls import path

from .views import meetings, meeting, new

urlpatterns = [
    path('', meetings, name='meetings'),
    path('meeting/<int:id>', meeting, name='meeting'),
    path('new', new, name='new')
]