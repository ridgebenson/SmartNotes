from django import forms
from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'content': forms.Textarea(attrs={'class': 'form-control my-5'})
        }
        labels = {
            'title': 'Title',
            'content': 'Content'
        }
