from django.urls import path

from .views import meetings, meeting

urlpatterns = [
    path('', meetings, name='meetings'),
    path('meeting/<int:id>', meeting, name='meeting')
]