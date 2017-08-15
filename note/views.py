from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note
from datetime import datetime

class HomeView(ListView):
	model = Note

class NoteDetail(DetailView):
	model = Note

class NoteUpdate(UpdateView):
    model = Note
    fields = ['title', 'content', 'time_updated']
    template_name_suffix = '_update'

class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'content']
    template_name_suffix = '_create'

class NoteDelete(DeleteView):
    model = Note
    template_name_suffix = '_delete'
