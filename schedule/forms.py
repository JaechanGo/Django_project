from django import forms
from schedule.models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('title', 'date', 'professor', 'grade', 'meo', 'schedule_type', )


