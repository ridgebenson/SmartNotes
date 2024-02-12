from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import ListView, DetailView


# Create your views here.

class NotesListView(ListView):
    model = Notes
    template_name = 'notes_list.html'
    context_object_name = 'notes'


class NotesDetailView(DetailView):
    model = Notes
    template_name = 'notes_detail.html'
    context_object_name = 'note'


# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes_list.html', {'notes': all_notes})


# def detail(request, note_id):
#     try:
#         note = Notes.objects.get(pk=note_id)
#     except Notes.DoesNotExist:
#         raise Http404('Note does not exist')
#     return render(request, 'notes_detail.html', {'note': note})
