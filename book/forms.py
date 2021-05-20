from django import forms
from book.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'date', 'professor', 'grade', 'meo', 'schedule_type', )