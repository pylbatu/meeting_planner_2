from datetime import date
from django.forms import ModelForm, DateInput, TextInput
from django.core.exceptions import ValidationError

from .models import Meeting

class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={
                'type': 'date'
            })
        }

    def clean_date(self):
        dateParam = self.cleaned_data.get('date')
        if dateParam < date.today():
            raise ValidationError('Date must be not in the past')
        return dateParam