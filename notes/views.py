from django.shortcuts import render
from .models import Notes
from django.http import Http404


# Create your views here.

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes_list.html', {'notes': all_notes})


def detail(request, note_id):
    try:
        note = Notes.objects.get(pk=note_id)
    except Notes.DoesNotExist:
        raise Http404('Note does not exist')
    return render(request, 'notes_detail.html', {'note': note})
