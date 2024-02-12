from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.NotesListView.as_view()),
    path('notes/<int:note_id>', views.NotesDetailView.as_view()),
    ]