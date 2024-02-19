from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import NotesForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class NotesCreateView(CreateView):
    model = Notes
    # template_name = 'notes_form.html'
    # fields = ['title', 'content']
    form_class = NotesForm
    success_url = '/smart/notes'


class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    template_name = 'notes_list.html'
    context_object_name = 'notes'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()


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
