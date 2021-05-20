from django import forms
from book.models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('title', 'date', 'professor', 'grade', 'meo', 'schedule_type', )